#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle_custom has been called")
    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2
    i = 0

    print('#######: ', request.duration)
    while i <= request.duration: 
        my_pub.publish(move_circle)
        rate.sleep()
        i=i+1
        
    move_circle.linear.x = 0
    move_circle.angular.z = 0
    my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_bb8_in_circle_custom")
    
    response = MyCustomServiceMessageResponse()
    response.success = True
    return response # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_circle_custom_server') 
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_circle_custom Ready")
rospy.spin() # mantain the service open.



