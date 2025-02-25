import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LoggerNode(Node):
    def __init__(self):
        super().__init__('logger_node')
        self.subscription = self.create_subscription(String, '/attitude_status', self.log_callback, 10)

    def log_callback(self, msg):
        status = msg.data
        self.get_logger().info(f"Logged attitude status: {status}")
        with open("attitude_log.txt", "a") as log_file:
            log_file.write(status + "\n")

def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
