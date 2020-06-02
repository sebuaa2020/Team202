#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
#include <stdio.h>
#include <termios.h>

int getch()
{
    int ch;
    struct termios oldt, newt;
    tcgetattr(STDIN_FILENO, &oldt);
    // save ths old
    newt = oldt;
    newt.c_lflag &= ~(ICANON);
    newt.c_lflag &= ~(ECHO);
    // ICANON: start stdin handling
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    // TCSANOW: modify the value immediatly
    // STDIN_FILENO:
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return ch;
}

const float linear_vel = 0.1;
const float angular_vel = 0.1;
const int k_vel = 3;

int main(int argc, char* argv[])
{
    ros::init(argc, argv, "manual_ctrl");

    printf("手动控制指令： \n");
    printf("w/W - 前进 \t");
    printf("s/S - 倒车 \n");
    printf("a/A - 左平移 \t");
    printf("d/D - 右平移 \n");
    printf("q/Q - 左转 \t");
    printf("e/E - 右转 \n");
    printf("SPACE - 刹车 \t");
    printf("ESC - 退出 \n");
    printf("------------- \n");

    ros::NodeHandle n;
    ros::Publisher cmd_vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

    geometry_msgs::Twist base_cmd, prev_cmd;
    base_cmd.linear.x = 0;
    base_cmd.linear.y = 0;
    base_cmd.angular.z = 0;

    prev_cmd.linear.x = 0;
    prev_cmd.linear.y = 0;
    prev_cmd.angular.z = 0;

    while (n.ok()) {
        int key = getch();
        switch (key) {
        case 'w':
        case 'W':
            base_cmd.linear.x += linear_vel;
            if (base_cmd.linear.x > linear_vel * k_vel) {
                base_cmd.linear.x = linear_vel * k_vel;
            }
            break;
        case 's':
        case 'S':
            base_cmd.linear.x += -linear_vel;
            if (base_cmd.linear.x < -linear_vel * k_vel) {
                base_cmd.linear.x = -linear_vel * k_vel;
            }
            cmd_vel_pub.publish(base_cmd);
            break;
        case 'a':
        case 'A':
            base_cmd.linear.y += linear_vel;
            if (base_cmd.linear.y > linear_vel * k_vel) {
                base_cmd.linear.y = linear_vel * k_vel;
            }
            break;
        case 'd':
        case 'D':
            base_cmd.linear.y += -linear_vel;
            if (base_cmd.linear.y < -linear_vel * k_vel) {
                base_cmd.linear.y = -linear_vel * k_vel;
            }
            break;
        case 'q':
        case 'Q':
            base_cmd.angular.z += angular_vel;
            if (base_cmd.angular.z > angular_vel * k_vel) {
                base_cmd.angular.z = angular_vel * k_vel;
            }
            break;
        case 'e':
        case 'E':
            base_cmd.angular.z += -angular_vel;
            if (base_cmd.angular.z < -angular_vel * k_vel) {
                base_cmd.angular.z = -angular_vel * k_vel;
            }
            break;
        case ' ':
        case 0x1B:
            base_cmd.linear.x = 0;
            base_cmd.linear.y = 0;
            base_cmd.angular.z = 0;
            break;
        default:
            printf(" - UNDEFINED INSTRUCTION! \n");
        }
        cmd_vel_pub.publish(base_cmd);
        if (base_cmd.linear.x != prev_cmd.linear.x
            || base_cmd.linear.y != prev_cmd.linear.y
            || base_cmd.angular.z != prev_cmd.angular.z) {
            printf(" - linear.x= %.2f linear.y= %.2f angular.z= %.2f \n",
                base_cmd.linear.x, base_cmd.linear.y, base_cmd.angular.z);
            prev_cmd = base_cmd;
        }
        if (key == 0x1B) {
            printf("EXIT! \n");
            break;
        }
    }
    return 0;
}
