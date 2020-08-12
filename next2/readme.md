#	LDS-01

$ ls -l /dev/ttyUSB0  

$ sudo chmod a+rw /dev/ttyUSB0	

--------------------------------------------------------

$ cd catkin_ws/src

$ git clone github.com/ROBOTIS-GIT/hls_lfcd_lds_driver

$ cd ..

$ catkin_make

OR

$ sudo apt-get install ros-kinetic-hls-lfcd-lds-driver

------------------------------------------------------------

(새 터미널)

$ roslaunch hls_lfcd_lds_driver hlds_laser.launch

(새터미널)

$ rviz

(rviz 화면에서)

Global Options

->	Fixed Frame  laser

-> LaserScan (안보이면 Add(왼쪽하단)에서 찾아서 추가)

-> Topic  /scan

