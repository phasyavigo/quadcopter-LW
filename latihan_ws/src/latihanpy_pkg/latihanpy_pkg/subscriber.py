import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__("subscriber_node")
        self.publisher = self.create_subscription(String, "/ngobrol", self.sub, 10)
    
    def sub(self, msg):
        self.get_logger().info("Hai gais aku menerima angka " + msg.data + " dari topic /ngobrol")
      
def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
