#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class MoveBB8():
    
    def __init__(self):
        '''
        This is the constructor of the class. Here, we are defining several attributes:
        bb8_vel_publisher: Creates a Publisher for the /cmd_vel topic
        cmd: Contains a Twist message
        ctrl_c: Contains a boolean indicating if we have pressed Ctrl+C in order to stop the program
        rate: Contains the rate frequency        
        '''
        self.bb8_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)
        
    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuos publishing systems there is no big deal but in systems that publish only
        once it IS very important.
        """
        while not self.ctrl_c:
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(self.cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
        
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.stop_bb8()
        self.ctrl_c = True
        
    def stop_bb8(self):
        rospy.loginfo("shutdown time! Stop the robot")
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel()

    def move_bb8(self, moving_time, linear_speed=0.2, angular_speed=0.2):
        
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = angular_speed
        i = 0
        
        rospy.loginfo("Moving BB8!")
        while not self.ctrl_c and i <= moving_time:
            self.publish_once_in_cmd_vel()
            i = i+1
            self.rate.sleep()
            
        self.stop_bb8()
            
if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8()
    try:
        movebb8_object.move_bb8()
    except rospy.ROSInterruptException:
        pass

