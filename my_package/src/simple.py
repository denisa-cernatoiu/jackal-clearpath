#! /usr/bin/env python
# Specifying the interpreter to be used, every py file need to start with this line
# Start with this line

import rospy # import the rospy library for ROS
rospy.init_node("Friends") # initiating a node called Friends
rate = rospy.Rate(2) # creating a rate object of 2Hz
while not rospy.is_shutdown(): # endless loop until Ctrl+C
	print("How you dooin?")
	rate.sleep() # we sleep the needed time to maintain the Rate fixed above
# this program creates an endless loop that repets itself 2 times per second(2Hz) unitl somebody presses Ctrl+C in Shell

