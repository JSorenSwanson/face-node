## Training environment
ARG vers=16.04
FROM ubuntu:${vers}
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
    software-properties-common \ 
    apt-transport-https \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip3 -v
# Expose a port just to remember we can. 
EXPOSE 5000
# Slap a quick dir into container fs before we copy context over
RUN mkdir /develop
WORKDIR /develop
# Shoot context over to Daemon @ dir level
COPY . .
# Install container py package dependencies
RUN pip3 install -r requirements.txt

