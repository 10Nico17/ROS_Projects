#!/usr/bin/env python3

# Import the Python library for ROS
import rospy
# Import the Int32 message from the std_msgs package
from std_msgs.msg import Int32    
from geometry_msgs.msg import Twist


# Initiate a Node named 'topic_publisher'
rospy.init_node('topic_publisher')

# Create a Publisher object, that will publish on the /counter topic
# messages of type Int32
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    
                                           
# Set a publish rate of 2 Hz
rate = rospy.Rate(2)
# Create a variable of type Int32
move = Twist()

move.linear.x = 0.01
move.angular.z = 0.01

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  # Publish the message within the 'count' variable
  pub.publish(move)
  # Make sure the publish rate maintains at 2 Hz
  rate.sleep()     
                 

    
                  
