#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from simple_interfaces_pkg.msg import ComponentsStatus

class ComponentStatusPublisherNode(Node):#1
    def __init__(self):
        super().__init__('component_status_publisher_node')#2
        self.component_status_publisher_ = self.create_publisher(ComponentsStatus, 
                                                                'component_status', 
                                                                0)
        self.timer = self.create_timer(1.0, self.publish_component_status)
        self.get_logger().info("Component Status Publisher Node has been started.")

    def publish_component_status(self):
        msg = ComponentsStatus()
        msg.camera_is_ready = True
        msg.lidar_is_ready = True
        msg.motor_is_ready = True
        msg.debug_message = "All systems operational"
        self.component_status_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ComponentStatusPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

