import rclpy
from rclpy.node import Node
from sam_bot_description.srv import StartNavigation  
from geometry_msgs.msg import PoseStamped
from std_srvs.srv import SetBool

#ros2 launch nav2_bringup localization_launch.py map:=two_rooms_map2.yaml params_file:=src/sam_bot_description/config/nav2_params.yaml

#ros2 launch nav2_bringup navigation_launch.py params_file:=src/sam_bot_description/config/nav2_params.yaml use_sim_time:=true map_subscribe_transient_local:=true

#ros2 service call /start_navigation sam_bot_description/StartNavigation "{start: true}"

#ros2 run teleop_twist_keyboard teleop_twist_keyboard

#ros2 launch sam_bot_description display.launch.py

#ros2 run star_navigation star_nav

#ros2 launch slam_toolbox online_async_launch.py

#ros2 launch yolov8_bringup yolov8.launch.py 
 




class NavigationStarter(Node):

    def __init__(self):
        super().__init__('navigation_starter')
        self.start_navigation_service = self.create_service(
            StartNavigation, '/start_navigation', self.start_navigation_callback
        )
        self.navigation_goal_publisher = self.create_publisher(
            PoseStamped, '/goal_pose', 10
        )

    def start_navigation_callback(self, request, response):
        # When the /start_navigation service is called, send a navigation goal
        goal_pose = PoseStamped()
        goal_pose.header.stamp = self.get_clock().now().to_msg()
        goal_pose.header.frame_id = 'map'  # Set the frame ID according to your map frame
        goal_pose.pose.position.x = 2.0  # Set the desired X coordinate
        goal_pose.pose.position.y = 0.0  # Set the desired Y coordinate
        goal_pose.pose.position.z = 0.0  # Set the desired Y coordinate

        goal_pose.pose.orientation.x = 0.0  # Set the desired orientation (x)
        goal_pose.pose.orientation.y = 0.0  # Set the desired orientation (y)
        goal_pose.pose.orientation.z = 0.0  # Set the desired orientation (z)
        goal_pose.pose.orientation.w = 1.0  # Set the desired orientation (w)


        self.navigation_goal_publisher.publish(goal_pose)
        self.get_logger().info('Navigation goal sent!')

        # Populate the response with success status and goal pose
        response.success = True  # Set this based on your actual success criteria
        response.goal_pose = goal_pose

        return response


def main(args=None):
    rclpy.init(args=args)
    navigation_starter = NavigationStarter()
    rclpy.spin(navigation_starter)
    navigation_starter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
