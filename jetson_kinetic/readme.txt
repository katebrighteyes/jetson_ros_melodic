
* kinetic 설치는 jetpack 3.3 설치 후에..

$ sudo apt-get update

$ git clone https://github.com/jetsonhacks/installROSTX2.git

$ cd installROSTX2

$ ./installROS.sh -p ros-kinetic-desktop -p ros-kinetic-rgbd-launch

$ ./setupCatkinWorkspace.sh [optionalWorkspaceName]


터미널을 닫는다.


<< 테스트 >>

[TEST]

EXECUTE roscore 창을 새로 띄운 후 roscore 실행
$ roscore

turtle 또 다른 창에서 거북이 창 실행
$ rosrun turtlesim turtlesim_node

move 또 다른 창에서 키 동작 오퍼 기능 실행
$ rosrun turtlesim turtle_teleop_key

