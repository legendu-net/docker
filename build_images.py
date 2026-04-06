# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "dulwich>=1.1.0",
#     "tenacity>=9.1.4",
# ]
# ///

import datetime
import subprocess as sp
from dulwich.repo import Repo
from dulwich import porcelain
from tenacity import retry, stop_after_attempt, wait_exponential

DIRS = [
    "docker-base",
    "docker-golang",
    "docker-gophernotes",
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
    "docker-jupyterhub-cuda",
    "docker-jupyterhub-pytorch",
    "docker-tensorboard",
    "docker-jupyterhub-kotlin",
    "docker-jupyterhub-ganymede",
    "docker-rustpython",
]


def tag_date(tag: str) -> str:
    """Suffix a tag with the current date as a 6-digit string.

    :param tag: A tag of Docker image.
    :return: A new tag.
    """
    return tag + datetime.datetime.now().strftime("_%m%d%H")


@retry(
    stop=stop_after_attempt(3), wait=wait_exponential(multiplier=60, min=60, max=300)
)
def push_image(image: str):
    sp.run(
        ["docker", "push", image],
        shell=False,
        check=True,
    )


def _build_image(dir_: str, tags: str | list[str]):
    if isinstance(tags, str):
        tags = [tags]
    image = dir_.replace("docker-", "dclong/")
    print(f"\n\nBuilding the Docker image {image}...")
    cmd = ["docker", "build", dir_]
    for tag in tags:
        cmd.append("-t")
        cmd.append(f"{image}:{tag}")
    sp.run(cmd, shell=False, check=True)
    for tag in tags:
        push_image(f"{image}:{tag}")


def is_no_diff() -> bool:
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
    if is_no_diff():
        tags.append("latest")
    tags.extend([tag_date(tag) for tag in tags])
    print("Building Docker images using tags:", ", ".join(tags), "\n")
    for dir_ in DIRS:
        _build_image(dir_, tags=tags)


if __name__ == "__main__":
    build_images()
