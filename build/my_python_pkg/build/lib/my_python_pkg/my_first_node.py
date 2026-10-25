#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("python_test")
        self.get_logger().info("Hello World")
        self.create_timer(
            timer_period_sec=1.0,
            callback=self.timer_callback)
        
        self.counter_ = 0

    def timer_callback(self):
        self.get_logger().info(f"Timer: Hello: {str(self.counter_)}")
        self.counter_ +=1


def main(args=None): 
    rclpy.init(
        args=args
    )
    
    # node = Node("python_test")
    # node.get_logger().info("Hello World!")
    node = MyNode()

    # Keeps node alive until Ctrl+C is pressed
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()