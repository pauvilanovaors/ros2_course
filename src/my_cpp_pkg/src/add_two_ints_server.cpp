
#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

class AddTwoIntsServerNode: public rclcpp::Node
{
    public:
        AddTwoIntsServerNode(): Node("add_two_ints_server"),
        {
            server_ = this->create_service<example_interfaces::src::AddTwoInts>("add_two_ints", );
        }
    
    private:
        rclcpp::Servic<example_interfaces::srv::AddTwoInts>::SharedPtr server_;
};


int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyNode>();
    // RCLCPP_INFO(node->get_logger(), "Hello world");

    rclcpp::spin(node);
    rclcpp::shutdown();
    
    return 0;
}