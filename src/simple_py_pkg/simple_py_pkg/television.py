#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class ChannelNode(Node):#1
    def __init__(self):
        super().__init__('channel_node')#2
        self.declare_parameter('greeting', 'Hİ!')
        self.greeting_ = "Hİ!"
        self.publishers_ = self.create_publisher(String, 'channel_something', 10)
        self.timer_ = self.create_timer(0.5, self.publish_channel)
        self.get_logger().info('ChannelNode has been published!.') 
    
    def publish_channel(self):
        msg = String()
        msg.data = str(self.greeting_)+ " Welcome to the Channel Node"
        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ChannelNode()#3
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

