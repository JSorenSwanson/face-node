## WSL Cuda Edge driver notes compiled from nV docs
#  https://docs.nvidia.com/cuda/wsl-user-guide/index.html
#  https://developer.nvidia.com/cuda/wsl – Edge Cuda WSL drivers necessary for paravirtualization of GPU res thru WSL 
##  Note:Do not install any Linux display driver in WSL. The Windows Display Driver will install both the regular driver components for native Windows and for WSL support.

## This will install the necessary deb libs for Ubuntu-18.04 to support CUDA on WSL. 
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
curl -s -L https://nvidia.github.io/libnvidia-container/experimental/$distribution/libnvidia-container-experimental.list | sudo tee /etc/apt/sources.list.d/libnvidia-container-experimental.list
apt-get update
apt-get install -y nvidia-docker2