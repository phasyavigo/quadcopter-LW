import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AttitudeMonitor(Node):
    def __init__(self):
        super().__init__('attitude_monitor')
        self.subscription = self.create_subscription(String, '/imu_data', self.listener_callback, 10)
        self.publisher = self.create_publisher(String, '/attitude_status', 10)

    def listener_callback(self, msg):
        try:
            parts = msg.data.split(',')
            roll = float(parts[0])
            pitch = float(parts[1])
            yaw = float(parts[2])
        except Exception as e:
            self.get_logger().error("Gagal mem-parse data IMU")
            return
        
    
        if abs(roll) < 10 and abs(pitch) < 10:
            status = "Stable"
        else:
            status = "Unstable"
        
        status_msg = String()
        status_msg.data = status
        self.publisher.publish(status_msg)
        self.get_logger().info(f"Attitude status: {status} (roll: {roll:.2f}, pitch: {pitch:.2f}, yaw: {yaw:.2f})")

def main(args=None):
    rclpy.init(args=args)
    node = AttitudeMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
