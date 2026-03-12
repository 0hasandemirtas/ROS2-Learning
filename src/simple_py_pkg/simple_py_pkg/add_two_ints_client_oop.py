#!/usr/bin/env python3

from platform import node

import rclpy
from rclpy.node import Node
from functools import partial
from example_interfaces.srv import AddTwoInts

class AddTwoInstsClientNode(Node):#1
    def __init__(self):
        super().__init__('add_two_ints_client')#2
        self.call_add_two_ints_service(7,8)
        self.call_add_two_ints_service(71,81)
        self.call_add_two_ints_service(72,85)
        self.call_add_two_ints_service(73,86)
        self.call_add_two_ints_service(74,87)


    def call_add_two_ints_service(self,a ,b):
        client_ = self.create_client(AddTwoInts, "add_two_ints")
        while not client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Service not available, waiting again...")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = client_.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info("Result :" + str(response.sum))

        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoInstsClientNode()#3
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

