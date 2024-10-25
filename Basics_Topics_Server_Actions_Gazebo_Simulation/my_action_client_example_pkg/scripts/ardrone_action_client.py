#!/usr/bin/env python3

'''
The code to call an action server is very simple:

    First, you create a client connected to the action server you want:

    client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
    client = actionlib.SimpleActionClient('/the_action_server_name', the_action_server_message_python_object)


    * First parameter is the name of the action server you want to connecto to.
    * Second parameter is the type of action message that it uses. The convention goes as follows:

    If your action message file was called **Ardrone.action**, then the type of action message you must specify is **ArdroneAction**. The same rule applies to any other type (**R2Action**, for an **R2.action** file or **LukeAction** for a **Luke.action** file). In our exercise it is:

    client = actionlib.SimpleAction('/ardrone_action_server', ArdroneAction)

    Then you create a goal:

    goal = ArdroneGoal()

    Again, the convention goes as follows:

    If your action message file was called Ardrone.action, then the type of goal message you must specify is ArdroneGoal(). The same rule applies to any other type (R2Goal() for an R2.action file or LukeGoal() for a Luke.action file).
    Because the goal message requires to provide the number of seconds taking pictures (in the nseconds variable), you must set that parameter in the goal class instance:

    goal.nseconds = 10

    Next, you send the goal to the action server:

    client.send_goal(goal, feedback_cb=feedback_callback)

    That sentence calls the action. In order to call it, you must specify 2 things:

        The goal parameters

        A feedback function to be called from time to time to know the status of the action.


        At this point, the action server has received the goal and started to execute it (taking pictures for 10 seconds). Also, feedback messages are being received. Every time a feedback message is received, the feedback_callback function is executed.

    Finally, you wait for the result:

    client.wait_for_result()
'''



import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# initializes the action client node
rospy.init_node('drone_action_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
goal.nseconds = 10 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()  # would cancel the goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
# status = client.get_state()
# check the client API link below for more info

client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))
