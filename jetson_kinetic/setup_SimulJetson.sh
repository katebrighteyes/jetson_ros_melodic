#!/bin/bash

sudo apt-get install ros-kinetic-ar-track-alvar-msgs

sudo apt autoremove

sudo apt-get install ros-kinetic-turtlebot3 -y

sudo apt-get install ros-kinetic-joy ros-melodic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-melodic-rosserial-server ros-melodic-rosserial-client ros-melodic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation ros-kinetic-interactive-markers -y

sudo apt-get install ros-kinetic-turtlebot3-* -y
sudo apt-get install ros-kinetic-gazebo -y
sudo apt-get install ros-kinetic-turtlebot3-gazebo -y
sudo apt-get install ros-kinetic-gazebo-ros-pkgs ros-melodic-ros-control -y
sudo apt install ros-kinetic-slam-gmapping -y

sudo apt-get install ros-kinetic-gazebo-ros -y
sudo apt-get install ros-kinetic-gazebo-dev -y
sudo apt-get install ros-kinetic-gazebo-msgs -y
