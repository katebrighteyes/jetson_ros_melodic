#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees, pi, sin, cos
from actionlib_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped
from copy import deepcopy
from ros_darknet_test.msg import Infodata2

import tf
import numpy as np
import rospy
import string
import math
import time
import sys

from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseActionResult
from actionlib_msgs.msg import GoalStatusArray
from geometry_msgs.msg import PoseStamped
    
class MyGoalPose:
    x = 0.
    y = 0.
    deg = 0.
    
def statusCB(data):
    if data.status.status == 3: # reached
        print('reached')
 
moveBottle = 0
moveApple = 0
       
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
    
def moveTo(pos):
    goalMsg = PoseStamped()
    goalMsg.header.frame_id = "map"

    th_rad = pos.deg * pi/180.
    q = tf.transformations.quaternion_from_euler(0.0, 0.0, th_rad)
        
    goalMsg.pose.orientation.x = q[0]
    goalMsg.pose.orientation.y = q[1]
    goalMsg.pose.orientation.z = q[2]
    goalMsg.pose.orientation.w = q[3]
        
    #goalMsg.pose.orientation.z = 0.0
    #goalMsg.pose.orientation.w = 1.0
    time.sleep(1)
    goalMsg.header.stamp = rospy.Time.now()
    goalMsg.pose.position.x = pos.x
    goalMsg.pose.position.y = pos.y
    pub.publish(goalMsg)  
    
rospy.init_node('my_goal_test', anonymous=False)

pos_start = MyGoalPose()
pos_start.x = -1.98
pos_start.y = 0.22
pos_start.deg = -15.00

pos_bottle = MyGoalPose()
pos_bottle.x = -0.55
pos_bottle.y = 0.52
pos_bottle.deg = 25.00

pos_apple = MyGoalPose()
pos_apple.x = 0.51
pos_apple.y = -1.03
pos_apple.deg = 0.21


print('move to pos_start - x:{} y:{} th_deg:{}'.format(pos_start.x, pos_start.y, pos_start.deg))

sub = rospy.Subscriber('move_base/result', MoveBaseActionResult, statusCB, queue_size=10)
pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)  

det_sub = rospy.Subscriber('detdata', Infodata2, detresCB, queue_size=10)
   
moveTo(pos_start)
'''                     
goalMsg = PoseStamped()
goalMsg.header.frame_id = "map"

th_rad = pos.deg * pi/180.
q = tf.transformations.quaternion_from_euler(0.0, 0.0, th_rad)
    
goalMsg.pose.orientation.x = q[0]
goalMsg.pose.orientation.y = q[1]
goalMsg.pose.orientation.z = q[2]
goalMsg.pose.orientation.w = q[3]
    
#goalMsg.pose.orientation.z = 0.0
#goalMsg.pose.orientation.w = 1.0
time.sleep(1)
goalMsg.header.stamp = rospy.Time.now()
goalMsg.pose.position.x = pos.x
goalMsg.pose.position.y = pos.y
pub.publish(goalMsg)  
'''  
                 
rospy.spin()

