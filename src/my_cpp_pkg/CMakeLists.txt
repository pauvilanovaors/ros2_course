cmake_minimum_required(VERSION 3.20)

project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
target_link_libraries(cpp_node PRIVATE
  rclcpp::rclcpp
)

add_executable(robot_news_station src/robot_news_station.cpp)
target_link_libraries(robot_news_station PRIVATE
  rclcpp::rclcpp
  example_interfaces::example_interfaces
)

add_executable(smartphone src/smartphone.cpp)
target_link_libraries(smartphone PRIVATE
  rclcpp::rclcpp
  example_interfaces::example_interfaces
)


install(
  TARGETS
    cpp_node
    robot_news_station
    smartphone
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()