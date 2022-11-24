#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees, pi, sin, cos
from actionlib_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped
from copy import deepcopy
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
    
rospy.init_node('my_goal_test', anonymous=False)

pos = MyGoalPose()
pos.x = -1.67
pos.y = -0.81
pos.deg = 45.28

print('move to x:{} y:{} th_deg:{}'.format(pos.x, pos.y, pos.deg))

sub = rospy.Subscriber('move_base/result', MoveBaseActionResult, statusCB, queue_size=10)
pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)  
                         
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
                 
rospy.spin()
