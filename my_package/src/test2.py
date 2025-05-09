#! /usr/bin/env python

import rospy 
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
def my_callback(request):
	move_circle.linear.x = 0.2
	move_circle.angular.z = 0.2
	my_pub.publish(move_circle)
	retrun EmptyResponse()

rospy.init_node('move_in_circle')
my_service = rospy.Service('/move_tb3_in_circle',Empty, mycallback)
my_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
move_circle = Twist()
rospy.loginfo("Cerc la dreapta")
rospy.spin()
