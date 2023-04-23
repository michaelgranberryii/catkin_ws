#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def publish_velocity():
    # Initialize the node and set the publisher topic
    rospy.init_node('velocity_publisher')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Set the rate of publishing to 10 Hz
    rate = rospy.Rate(10)

    # Create a Twist message to hold the velocity command
    velocity_cmd = Twist()
    # velocity_cmd.linear.x = 0.1 # set linear x velocity to 0.1 m/s
    # velocity_cmd.linear.y = 0.1
    velocity_cmd.angular.z = -0.8
    # velocity_cmd.angular.x = 0.1

    # Loop until the node is shut down
    while not rospy.is_shutdown():
        # Publish the velocity command
        pub.publish(velocity_cmd)

        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_velocity()
    except rospy.ROSInterruptException:
        pass
