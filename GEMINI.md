# Gemini CLI - Docker Images Project Context

This repository contains a collection of Dockerfiles and supporting scripts
for building a hierarchical set of Docker images under the `dclong/` namespace.
These images provide environments for basic Linux usage, various programming languages,
and complex data science tools like JupyterLab and JupyterHub.

## Project Overview

- **Namespace:** `dclong/`
- **Base OS:** Ubuntu (starting from `dclong/base`, which is based on `ubuntu:25.10`).
- **Architecture:** Hierarchical. Images build upon each other to share common configurations and tools.
  - `docker-base` (Root)
  - `docker-rust`, `docker-python`, `docker-nodejs` (Language-specific)
  - `docker-jupyterlab`, `docker-jupyterhub` (Application-specific)
- **Build Automation:** A centralized `build_images.py` script (from `legendu-net/github_actions_scripts`) manages the build order and tagging strategy.

## Building and Running

### Build Automation

The primary way to build and push images is using a centralized `build_images.py` script.
It requires Python 3.14+ and the `uv` package manager.

```bash
# Build and push images in the defined order
curl -sSL https://raw.githubusercontent.com/legendu-net/github_actions_scripts/main/build_images.py | uv run --script -
```

The script:

1. Determines tags based on the branch state (e.g., `next`, `latest`, and timestamped versions).
1. Iterates through the predefined `DIRS` list in the remote script to ensure parent images are built before children.
1. Builds each image using `docker build`.
1. Pushes the images to the registry.

### Manual Build

To build a specific image manually,
run `./build.sh` in the corresponding directory.

## Development Conventions

### Image Hierarchy

When adding a new image or modifying an existing one,
respect the hierarchy defined in the centralized `build_images.py` script.
Always use the `:next` tag for parent images during development.

### Layer Optimization

To keep image sizes minimal,
always purge package manager caches at the end of each `RUN` layer that performs installations.

- **Standard Practice:** Use the `/scripts/sys/purge_cache.sh` script (copied from `docker-base`).

```dockerfile
RUN apt-get update \
    && apt-get install -y some-package \
    && /scripts/sys/purge_cache.sh
```

### Script and Setting Management

- **Scripts:** Each image folder typically contains a `scripts/` directory.
  These are copied to `/scripts/` in the container.
- **Settings:** Configuration files (e.g., for JupyterLab) are often stored in a `settings/` directory
  and copied to the appropriate location in the container.

### Shell Configuration

The base image configures `bash` with specific options:

```dockerfile
SHELL ["/bin/bash", "-O", "extglob", "-c"]
```

This enables extended globbing for more powerful file matching in `RUN` commands.

## Key Files

- `docker-base/Dockerfile`: The foundation image containing common utilities and the `purge_cache.sh` script.
- `docker-base/scripts/sys/purge_cache.sh`: A comprehensive cache-clearing script used across all images.