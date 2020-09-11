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
  <p> Docker repository for this project can be found at https://hub.docker.com/repository/docker/nsoren/face-node. I won't be configuring automatic image building until our group understands how to use Docker as a group.</p>
     
   https://code.visualstudio.com/docs/remote/containers-tutorial
  
  <p>Containers can then be executed as services from project root directory via:
  </div>

  ```
  $ docker-compose run {SERVICE}
  ```

TODO: FINISH THIS README WITH TEAM
  Services are defined in docker-compose.yml and are defined as: 
  eye_buffer: Recognition
  flask_rack: Lightweight webserver 
  train_station: Model training 
   </p>
</div>
<div align= "center">
  <div align="left">
  <h4>0. Configuration</h4>
  <p> 
  <b>0.1</b>
  First, you'll need to either configure your python environment locally or pull the linked Docker image environment (recommended.)<br/>
  <b>0.2</b> 
  Once you've your container running and you're attached to it remotely, execute this in the root container volume directory:
  
  ```
  $ pip3 install -r requirements.txt 
  ```
  </div>
  <div align="left">
  
  <h4>1. Training (relevant instructs from forked repo)</h4>

  ```
  $ python3 train_mask_detector.py --dataset dataset
  ```
  <h4> 2. Detection (see notes in detect_mask_video.py)</h4>
  <i>Check comments in detect_mask_video.py for notes on configuring OpenCV call to buffer frame data from VideoStream.</i> 

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
