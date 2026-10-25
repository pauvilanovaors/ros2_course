#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node):
    def __init__(self):
        super().__init__("smartphone")

        self.subscriber_ = self.create_subscription(
            String,
            "robot_news",
            self.callback_robots_news, # Callback triggered when a new data is published in the topic from the publisher (robot_news_station.py)
            10
        )

        self.get_logger().info("Subscriber Node created")

    def callback_robots_news(self, msg: String):
        self.get_logger().info(msg.data)


def main(args=None): 
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()