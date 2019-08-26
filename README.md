# ros_melodic

Melodic for Nano
설치
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop

참고 혹시 설치 관련 오류가 나면
ps -ef | grep apt
sudo kill [apt를 사용하는 프로세스]
sudo apt install ros-melodic-desktop
sudo rm /var/lib/dpkg/lock-frontend
sudo apt install ros-melodic-desktop
sudo rm /var/lib/dpkg/lock
sudo apt install ros-melodic-desktop

의존성 설치 및 추가 패키지 설치
sudo rosdep init 
rosdep update
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc 
source ~/.bashrc
sudo apt-get install cmake python-catkin-pkg python-empy python-nose python-setuptools libgtest-dev python-rosinstall python-rosinstall-generator python-wstool build-essential git

최종 환경 설정
cd ~/catkin_ws/
catkin_make
mkdir -p ~/catkin_ws/src 
cd ~/catkin_ws/
catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc 
source ~/.bashrc

Melodic for Xavier, TX2 (Jetpack 4.2.1)
설치
git clone https://github.com/jetsonhacks/installROSXavier.git

cd installROSXavier/
ls
./installROS.sh -p ros-melodic-desktop -p ros-melodic-rgbd-launch
./setupCatkinWorkspace.sh

* 터미널을 닫는다.

테스트
======================================
[TEST]

1) EXECUTE roscore 

$ roscore

2) turtle
$ rosrun turtlesim turtlesim_node

3) move
$ rosrun turtlesim turtle_teleop_key

