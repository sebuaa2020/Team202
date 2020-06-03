#ifndef FUNCTION_H
#define FUNCTION_H

#include "gmain.h"
// namespace robot {
// 将机器人当前位置保存为新航点
void AddNewWaypoint(std::string inStr);

// 跟随模式开关
void FollowSwitch(bool inActive, float inDist);
void Speak(std::string );

// 添加航点关键词
void InitKeyword();

// }
#endif