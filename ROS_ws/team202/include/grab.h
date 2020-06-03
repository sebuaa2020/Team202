#ifndef GRAB_H
#define GRAB_H

#include "gmain.h"
#include "function.h"
#include "exception_handler.h"


// 物品抓取模式开关
void GrabSwitch(bool inActive);

// 物品递给开关
void PassSwitch(bool inActive);


// 物品抓取状态
void GrabResultCallback(const std_msgs::String::ConstPtr& res);


// 物品递给状态
void PassResultCallback(const std_msgs::String::ConstPtr& res);


void xxgrab();
void xxpass();

#endif
