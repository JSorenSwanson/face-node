# Ripped from NVIDIA dev center download area – this will extract the cuda 10.1 drivers into the env for use with Tensorflow.
# If you don't already have them, grab them @ https://developer.nvidia.com/cuda-10.1-download-archive-base?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal
dpkg -i cuda-10.1.deb
apt-key add /var/cuda-libraries-10-1/7fa2af80.pub
apt-get update -y
apt-get install cuda -y