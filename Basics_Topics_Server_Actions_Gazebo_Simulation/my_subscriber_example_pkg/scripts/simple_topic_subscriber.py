#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32 



# Define a function called 'callback' that receives a parameter 
# Print the value 'data' inside the 'msg' parameter
def callback(msg): 
  print (msg.data)

# Initiate a Node called 'topic_subscriber'
# Create a Subscriber object that will listen to the /counter
# topic and will cal the 'callback' function each time it reads


rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/counter', Int32, callback)

# Create a loop that will keep the program in execution

rospy.spin()


