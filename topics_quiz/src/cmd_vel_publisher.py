#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
	x=msg.ranges[90]
	y=msg.ranges[180]
	z=msg.ranges[]
	move = Twist()
	
	if x > 1.0:
		move.linear.x=0.5
	else:
		move.angular.z=0.5
	if y < 1.0:
		move.angular.z = -0.5
	if z < 1.0:
		move.angular.z = 0.5
	pub.publish(move)
  


rospy.init_node('cmd_write')

pub = rospy.Publisher('/cmdv',  Twist, queue_size=1)
sub = ropsy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
