#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
	print(msg.header)
	print(msg.pose)

rospy.init_node('scan__subs')
sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
