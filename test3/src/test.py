#/usr/bin/env python

import rospy
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

def feedback_callback(feedback):

        if command == "TAKEOFF":
            for i in range(5): 
                self.server.publish_feedback(self.feedback)
                rate.sleep()

            while not rospy.is_shutdown() and not self.server.is_preempt_requested():
                self.server.publish_feedback(self.feedback)
                rate.sleep()

        elif command == "LAND":
            for i in range(5): 
                self.server.publish_feedback(self.feedback)
                rate.sleep()
            rospy.loginfo("Drone has landed.")


        self.server.set_succeeded(self.result)

if name == 'main':
    rospy.init_node('drone_command_server')
    server = DroneCommandActionServer()
    rospy.spin()
