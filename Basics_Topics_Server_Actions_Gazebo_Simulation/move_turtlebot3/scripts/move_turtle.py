#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg  import LaserScan 
from geometry_msgs.msg import Twist


def callback(msg): 
  print(msg.ranges[360]) 

#If the distance to an obstacle in front of the robot is bigger than 1 meter, the robot will move forward
  if msg.ranges[360] > 1.0:
      move.linear.x = 0.1
      move.angular.z = 0.0

#If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will turn left
  if msg.ranges[360] < 1.0: 
      move.linear.x = 0.0
      move.angular.z = 0.2
        
#If the distance to an obstacle at the left side of the robot is smaller than 0.3 meters, the robot will turn right
  if msg.ranges[719] < 1.0:
      move.linear.x = 0.0
      move.angular.z = -0.2
        
#If the distance to an obstacle at the right side of the robot is smaller than 0.3 meters, the robot will turn left
  if msg.ranges[0] < 1.0:
      move.linear.x = 0.0
      move.angular.z = 0.2
      
  pub.publish(move)

      

rospy.init_node('laser_scan_node')
sub = rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()




