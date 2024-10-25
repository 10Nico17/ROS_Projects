roslaunch iri_wam_gazebo main.launch
roslaunch unit_5_services my_robot_arm_demo.launch
--------------------------------------------
roslaunch bb_8_gazebo main.launch
roslaunch unit_5_services start_bb8_move_in_circle_service_server.launch 
roslaunch unit_5_services call_bb8_move_in_circle_service_server.launch 
--------------------------------------------
# Custom Server message:
roslaunch bb_8_gazebo main.launch
roslaunch unit_5_services start_bb8_move_custom_service_server.launch
roslaunch unit_5_services call_bb8_move_custom_service_server.launch
--------------------------------------------
# Create a python class
roslaunch bb_8_gazebo main.launch
rosrun unit_5_services bb8_move_circle_class.py
--------------------------------------------
# Use Python class in Server and Client
roslaunch unit_5_services bb8_move_circle_service_server.launch 
rosservice call /move_bb8_in_circle "duration: 5"
--------------------------------------------
