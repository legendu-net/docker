# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "dulwich>=1.1.0",
#     "tenacity>=9.1.4",
# ]
# ///

import argparse
import datetime
from pathlib import Path
import subprocess as sp
import sys
from dulwich.repo import Repo
from dulwich import porcelain
from dulwich.diff_tree import tree_changes
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


def changed_files_between(commit1: str, commit2: str) -> list[Path]:
    """Get a unique list of changed files between 2 commits.

    :param commit1: The first commit ID.
    :param commit2: The second commit ID.
    :return: A unique list of changed files.
    """
    repo = Repo(".")
    c1 = repo[commit1.encode()]
    c2 = repo[commit2.encode()]
    changes = tree_changes(repo.object_store, c1.tree, c2.tree)
    files = set()
    for change in changes:
        if change.old.path:
            files.add(change.old.path.decode())
        if change.new.path:
            files.add(change.new.path.decode())
    return sorted(Path(file).resolve() for file in files)


def has_relevant_changes(commit1: str, commit2: str) -> bool:
    if not commit1 or not commit2:
        return True
    dirs = [Path(d).resolve() for d in DIRS]
    for p in changed_files_between(commit1, commit2):
        if any(p.is_relative_to(d) for d in dirs):
            return True
    return False


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


def build_images(commit1: str, commit2: str):
    if not has_relevant_changes(commit1, commit2):
        print("Skip building Docker images as there are no relavent changes.\n")
        return
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


def parse_args():
    """Parse command-line arguments.

    :return: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Build Docker images.")
    parser.add_argument(
        "-c1",
        "--commit1",
        dest="commit1",
        default="",
        help="The first commit ID (empty by default).",
    )
    parser.add_argument(
        "-c2",
        "--commit2",
        dest="commit2",
        default="",
        help="The second commit ID (empty by default).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    build_images(args.commit1, args.commit2)


if __name__ == "__main__":
    main()
