#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees, pi, sin, cos
from actionlib_msgs.msg import *
from geometry_msgs.msg import PoseWithCovarianceStamped
from copy import deepcopy
import tf

rospy.init_node('my_control_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

current_pose = PoseWithCovarianceStamped()

def callback(msg):
    current_pose = msg
    print(current_pose)
    
odom_sub = rospy.Subscriber('/amcl_pose', 
                            PoseWithCovarianceStamped, 
                            callback) 
                            
rospy.spin()
                               
