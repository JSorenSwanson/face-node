## WHAT IS THIS?? 
## This is a linear manifest that will be used to build an image. An image is kind of like an ISO, it represents a virtual environment that can be
## executed.
ARG vers=16.04
# Base image (Ubuntu Xenial)
FROM ubuntu:${vers}
# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8
# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# Grab and install packages necessary for training and testing recognition. 
RUN apt-get update && apt-get upgrade -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    python3-tk \
    python3 \
    python-pip \
    git \
    curl \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip3 -v