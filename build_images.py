# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "dulwich>=1.1.0",
#     "tenacity>=9.1.4",
# ]
# ///

import datetime
from pathlib import Path
import re
import subprocess as sp
import sys
from dulwich.repo import Repo
from dulwich import porcelain
from tenacity import retry, stop_after_attempt, wait_exponential

DIRS = [
    "docker-base",
    "docker-rust",
    "docker-rust-utils",
    "docker-rust-cicd",
    "docker-python-portable",
    "docker-python",
    "docker-python-nodejs",
    "docker-jupyterlab",
    "docker-jupyterhub",
    "docker-jupyterhub-jdk",
    "docker-jupyterhub-more",
    "docker-vscode-server",
    "docker-jupyterhub-ds",
    # "docker-gitpod",
    # "docker-jupyterhub-cuda",
    # "docker-jupyterhub-pytorch",
    "docker-tensorboard",
    "docker-jupyterhub-kotlin",
    # "docker-jupyterhub-ganymede",
    # "docker-rustpython",
]


def _update_base_image_tag_text(text: str) -> str:
    pattern_image = r"dclong/\w+(-\w+)?"
    text = re.sub(rf"(\nFROM {pattern_image})\n", r"\1:next\n", text)
    text = re.sub(rf"(\nCOPY --from={pattern_image}) ", r"\1:next ", text)
    return text


def test_update_base_image_tag_text():
    text = """
# NAME: dclong/rust-cicd
FROM dclong/python

RUN pip3 install github-rest-api

ENV RUSTUP_HOME=/usr/local/rustup PATH=/usr/local/cargo/bin:$PATH
COPY --from=dclong/rust /usr/local/rustup/ /usr/local/rustup/
COPY --from=dclong/rust \
        /usr/local/cargo/bin/rustc \
        /usr/local/cargo/bin/rustdoc \
        /usr/local/cargo/bin/cargo \
        /usr/local/cargo/bin/cargo-fmt \
        /usr/local/cargo/bin/rustfmt \
    /usr/local/cargo/bin/
COPY --from=dclong/rust-utils /usr/local/cargo/bin/cargo-criterion /usr/local/cargo/bin/
COPY --from=dclong/rust-utils /usr/bin/nperf /usr/bin/
COPY settings/sysctl.conf /etc/sysctl.conf
""".strip()
    text_truth = (
        text.replace(
            "FROM dclong/python",
            "FROM dclong/python:next",
        )
        .replace(
            "--from=dclong/rust-utils ",
            "--from=dclong/rust-utils:next ",
        )
        .replace(
            "--from=dclong/rust ",
            "--from=dclong/rust:next ",
        )
    )
    assert _update_base_image_tag_text(text) == text_truth


def _update_base_image_tag(dir_: str, tags: list[str]) -> None:
    if "latest" in tags:
        return
    dockerfile = Path(dir_) / "Dockerfile"
    text = dockerfile.read_text()
    dockerfile.write_text(_update_base_image_tag_text(text))


def _tag_date(tag: str) -> str:
    """Suffix a tag with the current date as a 6-digit string.

    :param tag: A tag of Docker image.
    :return: A new tag.
    """
    return tag + datetime.datetime.now().strftime("_%m%d%H")


@retry(
    stop=stop_after_attempt(3), wait=wait_exponential(multiplier=60, min=60, max=300)
)
def _push_image(image: str):
    sp.run(
        ["docker", "push", image],
        shell=False,
        check=True,
    )


def _build_image(dir_: str, tags: str | list[str]):
    if isinstance(tags, str):
        tags = [tags]
    _update_base_image_tag(dir_, tags)
    image = dir_.replace("docker-", "dclong/")
    print(f"\n\nBuilding the Docker image {image}...", flush=True)
    cmd = ["docker", "build", dir_]
    for tag in tags:
        cmd.append("-t")
        cmd.append(f"{image}:{tag}")
    sp.run(cmd, shell=False, check=True)
    for tag in tags:
        _push_image(f"{image}:{tag}")


def _is_no_diff() -> bool:
    """Check whether there is no difference between dev/main branches."""
    repo = Repo(".")
    url = repo.get_config().get(("remote", "origin"), "url").decode("utf-8")
    refs = porcelain.ls_remote(url).refs
    walker = repo.get_walker(
        include=[refs[b"refs/heads/dev"]],
        exclude=[refs[b"refs/heads/main"]],
    )
    return next(iter(walker), None) is None


def build_images():
    tags = ["next"]
    try:
        if _is_no_diff():
            tags.append("latest")
    except Exception:
        pass
    tags.extend([_tag_date(tag) for tag in tags])
    print("Building Docker images using tags:", ", ".join(tags), "\n", flush=True)
    failures = []
    for dir_ in DIRS:
        try:
            _build_image(dir_, tags=tags)
        except Exception as _:
            failures.append(dir_)
    if failures:
        sys.exit(f"\n\nError: failed to build images: {', '.join(failures)}\n")


if __name__ == "__main__":
    build_images()
