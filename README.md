<div align= "center">
  <h4>POC jumping-off</h4>
  <p>Training and recognition strategy used is forked from https://github.com/chandrikadeb7/Face-Mask-Detection/.
  As we learn more about the components used, we will break our application into microservices and implement our own 
  training and recognition strategy to suit our needs.
  </p>
</div>
<div align= "center">
  <h4>Environment</h4>
  <p> Docker repository for this project can be found at https://hub.docker.com/repository/docker/nsoren/face-node.</p>
  <p>Latest development container image can be pulled using:
  ```
  docker pull nsoren/face-node:init
  ```
   </p>
</div>
<div align= "center">
  <h4>Training and Detection (relevant instructs from forked repo)</h4>
  <p> 
  0. Configuration
  0.1. 
  First, you'll need to either configure your python environment locally or pull the linked Docker image environment (recommended.)
  0.2. 
  Once you've your container running and you're attached to it remotely, execute pip3 install -r requirements.txt to install python packages required by the modules. 

  1. Training
  ```
  $ python3 train_mask_detector.py --dataset dataset
  ```
  2. Detection (see notes in detect_mask_video.py)
  ```
  $ python3 detect_mask_video.py 
  ```
  </p>
  <h4>Direction</h4>
  <p>
    We'll start using this project scaffold to modify and improve the existing face detection model to serve our application requirements in our first iteration.
  </p>

</div>

## :+1: Credits
* MIT © [Chandrika Deb](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/LICENSE)
* [https://www.pyimagesearch.com/](https://www.pyimagesearch.com/)
* [https://www.tensorflow.org/tutorials/images/transfer_learning]
