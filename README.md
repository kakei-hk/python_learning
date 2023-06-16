# Python Learning


## Overview

This is a project for learning Python.

## Tested Environment
This project has been tested in the following environments.

- Windows + WSL2 (Ubuntu 20.04)

## How to Use
- Without devcontainer
  1. Build a docker image using docker-compose.
      ```
      $ dcoker-compose build
      ```
  2. Launch a container.
      ```
      $ docker-compose run dev
      ```
  3. You can execute scripts in the container.
  4. Exit the container.
      ```
      $ exit
      ```

- With devcontainer
  1. Execute "set_env.sh" and create .env to refer to your UID/GID.
      ```
      $ bash set_env.sh
      ```
  2. Select "Dev Containers: Open Folder in Container ..." in command palette (ctrl+p) and the root directory of this project.
     A docker image is built and a container is launched.
  3. You can execute scripts in the container with VScode functions.
  4. Exit the container selecting "Dev Containers: Reopen Folder in \<select your local environment \> ..." in command palette.