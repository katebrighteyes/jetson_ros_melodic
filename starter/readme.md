# ros_jetson_start

# USB CAM ROS


# Melodic #
  
ls -ltr /dev/video*

cd catkin_ws/src

git clone https://github.com/bosch-ros-pkg/usb_cam

**********************
if your usb camera is /dev/video1
go to 54 line of this page.
**********************

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



*************************************************
* if your usb camera is /dev/video1 
*************
nvidia@nvidia:~$ ls -ltr /dev/video*

crw-rw----+ 1 root video 81, 0  9월 18 23:46 /dev/video0

crw-rw----+ 1 root video 81, 3  9월 19 02:41 /dev/video1

nvidia@nvidia:~$ cd catkin_ws/src

nvidia@nvidia:~/catkin_ws/src$ grep -rn video0 *

usb_cam/launch/usb_cam-test.launch:3:    <param name="video_device" value="/dev/video0" />

usb_cam/nodes/usb_cam_node.cpp:92:    node_.param("video_device", video_device_name_, std::string("/dev/video0"));


** YOU HAVE TO MODIFY THOSE 2 LINES TO "/dev/video1" !!!!
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
