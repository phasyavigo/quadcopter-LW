import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class IMUPublisher(Node):
    def __init__(self):
        super().__init__('imu_publisher')
        self.publisher_ = self.create_publisher(String, '/imu_data', 10)
        self.timer = self.create_timer(1.0, self.publish_imu_data)

    def publish_imu_data(self):
        roll = random.uniform(-30, 30)
        pitch = random.uniform(-30, 30)
        yaw = random.uniform(-180, 180)
        msg = String()
        msg.data = f"{roll:.2f},{pitch:.2f},{yaw:.2f}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published IMU data: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = IMUPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
