# Install ros_melodic

## ROS melodic 설치 (Jetpack 4.x 버전 설치 이후)

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update

----------------------
if failed,,

https://keyserver.ubuntu.com/

input 
0xF42ED6FBAB17C654

then 

click the first link

and make ros.pgp

and try like this :

sudo apt-key add ros.pgp 

-----------------------

sudo apt install ros-melodic-desktop

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential 

sudo rosdep init

rosdep update

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

source ~/.bashrc

======================================================
# 테스트

##[TEST]

#1) EXECUTE roscore 

##창을 새로 띄운 후 roscore 실행 

roscore

#2) turtle
##또 다른 창에서 거북이 창 실행

rosrun turtlesim turtlesim_node

#3)move
##또 다른 창에서 키 동작 오퍼 기능 실행

rosrun turtlesim turtle_teleop_key


======================================

##workspace 만들기

wget https://raw.githubusercontent.com/katebrighteyes/jetson_ros_melodic/master/install_catkinws.sh

chmod 777 install_catkinws.sh

./install_catkinws.sh

##확인

ls ~/catkin_ws


## 패지키 만들기 시작

cd ~/catkin_ws/src

catkin_create_pkg ros_topic_test std_msgs roscpp



##터미널을 닫는다.

..소스 작성 후

cd

cd catkin_ws


catkin_make

컴파일 성공 후 실행

cd

cd catkin_ws

catkin make

source ./devel/setup.bash

rosrun ros_topic_test ros_pub_test




