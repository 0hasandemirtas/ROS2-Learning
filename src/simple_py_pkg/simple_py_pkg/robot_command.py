#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotCommandNode(Node):
    def __init__(self):
        super().__init__('robot_command_node')
        self.declare_parameter('command_to_publish')
        
        self.command_ = self.get_parameter('command_to_publish').value
        self.command_publisher_ = self.create_publisher(String, 'robot_command', 10)
        self.timer_ = self.create_timer(1.0, self.publish_command)
        self.get_logger().info('RobotCommandNode has been published!.') 


    def publish_command(self):  
        msg = String()
        msg.data = str(self.command_)
        self.command_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotCommandNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

