#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from simple_interfaces_pkg.srv import MultiplyTwoInts

class MultiplyTwoIntsServer(Node):
    def __init__(self):
        super().__init__('multiply_two_ints_server')

        self.server_ = self.create_service(MultiplyTwoInts, 'multiply_two_ints', self.multiply_two_ints_callback)
        self.get_logger().info('MultiplyTwoIntsServer is ready to multiply two integers!')

    def multiply_two_ints_callback(self, request, response):
        response.result = request.a * request.b
        self.get_logger().info("Result:" + str(response.result))

        return response




def main(args=None):
    rclpy.init(args=args)
    node = MultiplyTwoIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

