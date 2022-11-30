1. ros_darknet_test 폴더의 src 에 추가

cd catkin_ws/src/ros_darknet_test/src
ros_darknet_test3.py 와 my_goal_test2.py 파일 작성하기
chmod 777 *

2. ros_darknet_test 폴더에 msg 폴더 만들기

cd catkin_ws/src/ros_darknet_test
mkdir msg
cd msg
gedit Infodata2.msg

내용 작성하기

3. 빌드

cd catkin_ws
catkin_make

4. 검출할 대상 정하기
컵이나 병 혹은 과일, 마우스를 검출 시킨 후 어떤 라벨이 나오는지 확인하기
자신이 정한 라벨에 따라 my_goal_test2.py 의 detresCB 함수의 42 라인과 46 라인의 라벨 이름 변경하고 저장

--------
def detresCB(data):
    global moveBottle
    global moveApple
    print(data.label) 
    
    if data.label == "bottle" and moveBottle == 0:
        moveBottle = 1
        moveTo(pos_bottle)  
        print('move to pos_bottle - x:{} y:{} th_deg:{}'.format(pos_bottle.x, pos_bottle.y, pos_bottle.deg))
    elif data.label == "apple" and moveApple == 0:
        moveApple = 1
        moveTo(pos_apple)    
        print('move to pos_apple - x:{} y:{} th_deg:{}'.format(pos_apple.x, pos_apple.y, pos_apple.deg))        

-----------------
전달해준 동영상 참고하세요

5. 가제보 실행
roslaunch turtlebot3_gazebo turtlebot3_world.launch

6. 네비 실행
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml

7. moveto 예제 실행
rosrun ros_darknet_test my_goal_test2.py 

8. darknet test 실행

source ~/cvbridge_build_ws/devel/setup.bash
rosrun ros_darknet_test ros_darknet_test3.py

(혹시 안되면)
cd ~/cvbridge_build_ws
source install/setup.bash --extend
rosrun ros_darknet_test ros_darknet_test3.py


