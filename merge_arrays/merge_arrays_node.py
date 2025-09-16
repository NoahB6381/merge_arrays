import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MergeArraysNode(Node):
    def __init__(self):
        super().__init__('merge_arrays_node')
        self.mergedArray = self.create_publisher(Int32MultiArray, "merge", 10)
        self.array1 = self.create_subscription(Int32MultiArray, "array1", self.run1, 10)
        self.array2 = self.create_subscription(Int32MultiArray, "array2", self.run2, 10)
        
        self.arr1 = None
        self.arr2 = None
        
    def run1(self, msg):
        self.arr1 = msg.data
        self.merge()
        
    def run2(self, msg):
        self.arr2 = msg.data
        self.merge()
        
    def merge(self):
        if self.arr1 != None and self.arr2 != None:
            merged = sorted(self.arr1 + self.arr2)
            self.get_logger().info(f'Yeah you merged!!!: {merged}')

def main(args=None):
    rclpy.init(args=args)
    node = MergeArraysNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
