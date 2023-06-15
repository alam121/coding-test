#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleControlNode:
    def __init__(self):
        self.leader_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        self.follower_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=1)
        self.leader_pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.leader_pose_callback)
        self.follower_pose_sub = rospy.Subscriber('/turtle2/pose', Pose, self.follower_pose_callback)
        self.is_follower_moving = False
        self.leader_pose = Pose()
        self.follower_pose = Pose()

    def leader_pose_callback(self, msg):
        self.leader_pose = msg
        self.move_follower()

    def follower_pose_callback(self, msg):
        self.follower_pose = msg
        self.move_follower()

    def move_follower(self):
        distance = math.sqrt((self.leader_pose.x - self.follower_pose.x) ** 2 + (self.leader_pose.y - self.follower_pose.y) ** 2)

        if distance > 0.8:
            follower_cmd_vel = Twist()
            follower_cmd_vel.linear.x = 0.5 * (self.leader_pose.x - self.follower_pose.x)
            follower_cmd_vel.linear.y = 0.5 * (self.leader_pose.y - self.follower_pose.y)
            self.follower_pub.publish(follower_cmd_vel)
            self.is_follower_moving = True
        elif self.is_follower_moving:
            follower_stop_cmd = Twist()
            self.follower_pub.publish(follower_stop_cmd)
            self.is_follower_moving = False

    def run(self):
        rospy.spin()

rospy.init_node('turtle_control_node')
node = TurtleControlNode()
node.run()

