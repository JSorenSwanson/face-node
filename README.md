<div align= "center">
  <h4>POC jumping-off</h4>
  <div align="left">
  <p>Training and recognition strategy used is forked from https://github.com/chandrikadeb7/Face-Mask-Detection/.
  As we learn more about the components used, we will break our application into microservices and implement our own 
  training and recognition strategy to suit our needs.
  </p>
  </div>
</div>
<div align= "center">
  <h4>Environment</h4>
   <div align="left">
  <p> Docker repository for this project can be found at https://hub.docker.com/repository/docker/nsoren/face-node. I won't be configuring automatic image building until our group understands how to use Docker as a group if we decide to utilize it.</p>
     
   https://code.visualstudio.com/docs/remote/containers-tutorial
  
  <p>Development container image can be pulled using:
  </div>
    
  ```
  $ docker pull nsoren/face-node:init
  ```
   </p>
</div>
<div align= "center">
  <h4></h4>
  <div align="left">
  <p> 
  <h4>0. Configuration</h4>
  0.1
  First, you'll need to either configure your python environment locally or pull the linked Docker image environment (recommended.)
  0.2 
  Once you've your container running and you're attached to it remotely, execute this in the root container volume directory:
    
    pip3 install -r requirements.txt 
  
  </div>
  <div align="left">
  
  <h4>1. Training and Detection (relevant instructs from forked repo)</h4>

  ```
  $ python3 train_mask_detector.py --dataset dataset
  ```
  2. Detection (see notes in detect_mask_video.py)
  ```
  $ python3 detect_mask_video.py 
  ```
  </div>
  </p>
  <h4>~Direction</h4>
  <div align="left">
  <p>
    We'll start using this project scaffold to modify and improve the existing face detection model to serve our application requirements in our first iteration.
  </p>
  </div>
</div>

## :+1: Credits
* MIT © [Chandrika Deb](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/LICENSE)
* [https://www.pyimagesearch.com/](https://www.pyimagesearch.com/)
* [https://www.tensorflow.org/tutorials/images/transfer_learning]
