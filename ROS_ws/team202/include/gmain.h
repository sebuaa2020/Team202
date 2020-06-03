#ifndef GMAIN_H
#define GMAIN_H

#include <ros/ros.h>
#include <std_msgs/String.h>
#include "wpb_home_tutorials/Follow.h"
#include <geometry_msgs/Twist.h>
#include "xfyun_waterplus/IATSwitch.h"
#include <sound_play/SoundRequest.h>
#include "wpb_home_tutorials/Follow.h"
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <waterplus_map_tools/Waypoint.h>
#include <waterplus_map_tools/GetWaypointByName.h>
#include <tf/transform_listener.h>
#include <geometry_msgs/PoseStamped.h>
/* AAO	*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#define MSGBUFSIZ 1024    
/* AAO END	*/

#define STATE_READY     0
#define STATE_FOLLOW    1
#define STATE_ASK       2
#define STATE_GOTO      3
#define STATE_GRAB      4
#define STATE_COMEBACK  5
#define STATE_PASS      6

//namespace robot{


typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;
extern std::string strGoto;
extern sound_play::SoundRequest spk_msg;
extern ros::Publisher spk_pub;
extern ros::Publisher vel_pub;

extern std::string strToSpeak;
extern std::string strKeyWord;

extern ros::ServiceClient clientIAT;
extern xfyun_waterplus::IATSwitch srvIAT;
extern ros::ServiceClient cliGetWPName;
extern waterplus_map_tools::GetWaypointByName srvName;
extern ros::Publisher add_waypoint_pub;
extern ros::ServiceClient follow_start;
extern ros::ServiceClient follow_stop;
extern ros::ServiceClient follow_resume;
extern wpb_home_tutorials::Follow srvFlw;
extern ros::Publisher behaviors_pub;
extern std_msgs::String behavior_msg;

extern ros::Subscriber grab_result_sub;
extern ros::Subscriber pass_result_sub;
extern bool bGrabDone;
extern bool bPassDone;

extern int nState;
extern int nDelay;

extern std::vector<std::string> arKeyword;

//}


#endif