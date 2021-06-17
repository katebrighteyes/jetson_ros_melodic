# ros_jetson_start

# USB CAM ROS


# Melodic #
  
ls -ltr /dev/video*

cd catkin_ws/src

git clone https://github.com/bosch-ros-pkg/usb_cam



cd ..

sudo apt-get install ros-melodic-camera-info-manager libavcodec-dev libswscale-dev -y

catkin_make

source ~/catkin_ws/devel/setup.bash

rospack find usb_cam

sudo apt-get install ros-melodic-image-view


source ~/catkin_ws/devel/setup.bash

[1]

$ roslaunch usb_cam usb_cam-test.launch

[2]

$ rosrun rqt_graph rqt_graph



***************************************************


# Kinetic #
  
ls -ltr /dev/video*

cd catkin_ws/src

git clone https://github.com/bosch-ros-pkg/usb_cam

sudo apt-get install ros-indigo-camera-info-manager

source ~/catkin_ws/devel/setup.bash

rospack find usb_cam

sudo apt-get install ros-kinetic-image-view

roscore

roslaunch usb_cam usb_cam-test.launch

rosrun rqt_graph rqt_graph
