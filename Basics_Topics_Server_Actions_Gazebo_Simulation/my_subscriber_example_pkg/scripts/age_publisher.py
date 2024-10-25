#!/usr/bin/env python3

# Import the Python library for ROS
import rospy         
from my_subscriber_example_pkg.msg import Age 


# Initiate a Node named 'topic_publisher'
rospy.init_node('age_publisher')

# Create a Publisher object, that will publish on the /counter topic
# messages of type Int32
pub = rospy.Publisher('/Age', Age, queue_size=1)    



# Set a publish rate of 2 Hz
rate = rospy.Rate(2)
# Create a variable of type Int32
age = Age()


# Initialize 'count' variable
age.years = 10.0                     

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  # Publish the message within the 'count' variable
  pub.publish(age)
  # Make sure the publish rate maintains at 2 Hz
  rate.sleep()                             