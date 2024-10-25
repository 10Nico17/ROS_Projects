#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.

import sys

print('############ Client ##################')

rospy.init_node('service_server_client_bb8_circle')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
traj_by_name_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

# Create an object of type TrajByNameRequest
traj_by_name_object = EmptyRequest()

# Send through the connection the name of the trajectory to be executed by the robot
result = traj_by_name_service(traj_by_name_object)
# Print the result given by the service called
print(result)


