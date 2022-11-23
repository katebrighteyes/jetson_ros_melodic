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

rospy.init_node('my_position_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

current_pose = PoseWithCovarianceStamped()
convert_to_nparray = lambda o: np.array([o.x, o.y, o.z, o.w])
convert_to_deg = lambda o: [o[0], o[1], o[2]*180./pi]

def callback(msg):
    current_pose = msg
    #print(current_pose)
    #data = convert_to_deg(cur_pos_xyth(current_pose))
    #print(data)
    x, y, th_rad = cur_pos_xyth(current_pose)
    print('x:{} y:{} th_deg:{}'.format(x, y, th_rad*180./pi))
   
def cur_pos_xyth(pos):
    x = pos.pose.pose.position.x
    y = pos.pose.pose.position.y
    
    tmp = convert_to_nparray(pos.pose.pose.orientation)
    [_,_, th_rad] = tf.transformations.euler_from_quaternion(tmp)
    
    return x, y, th_rad    
    
odom_sub = rospy.Subscriber('/amcl_pose', 
                            PoseWithCovarianceStamped, 
                            callback) 


                        
rospy.spin()
                               
