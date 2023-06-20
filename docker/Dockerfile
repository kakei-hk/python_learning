FROM ubuntu:20.04

ARG USERNAME=developer
ARG GROUPNAME=developer
ARG UID=1000
ARG GID=1000
ARG PASSWORD=developer
RUN groupadd -g $GID $GROUPNAME \
    && useradd -m -s /bin/bash -u $UID -g $GID -G sudo $USERNAME \
    && echo $USERNAME:$PASSWORD | chpasswd  \
    && echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo 'Defaults exempt_group = sudo' >> /etc/sudoers

# Basic packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    vim \
    less \
    git \
    wget \
    unzip \
    openssh-client \
    pkg-config \
    gdb \
    clang-format \
    cmake \
    ninja-build

# Python packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3.8 \
    python3-pip
RUN pip3 install \
    numpy==1.24.2 \
    pandas==2.0.0 \
    matplotlib==3.7.1 \
    black==23.3.0 \
    flake8==6.0.0 \
    isort==5.12.0 \
    mypy==1.2.0 \
    mypy-extensions==1.0.0 \
    pytest==7.3.1 

