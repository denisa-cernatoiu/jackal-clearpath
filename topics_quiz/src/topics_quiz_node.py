import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(scan):
    twist = Twist()
    front = scan.ranges[len(scan.ranges)//2]
    right = scan.ranges[0]
    left = scan.ranges[-1]

    if front > 1:
        twist.linear.x = 0.5
        twist.angular.z = 0.0
    elif front < 1:
        twist.linear.x = 0.0
        twist.angular.z = 0.5
    elif right < 1:
        twist.linear.x = 0.0
        twist.angular.z = 0.5
    elif left < 1:
        twist.linear.x = 0.0
        twist.angular.z = -0.5

    pub.publish(twist)

rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
