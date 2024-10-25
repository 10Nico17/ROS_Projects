#!/usr/bin/env python3

import rospy
# Import the service message used by the service /trajectory_by_name
#from trajectory_by_name_srv.srv import TrajByName, TrajByNameRequest

from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest 


import sys
import rospkg

rospack = rospkg.RosPack()
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
print('traj: ',traj)

rospy.init_node('service_client_execute_trajectory')
rospy.wait_for_service('/execute_trajectory')

execute_traj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
execute_traj_object = ExecTrajRequest()

execute_traj_object.file = traj
result = execute_traj_service(execute_traj_object)

print(result)
