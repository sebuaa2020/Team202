# -*- encoding: utf-8 -*-
import socket
import subprocess
import os
import virtkey
import time


def control_shell(data):
    instruct = data.split(' ')
    # print(instruct[0], instruct[1])
    if instruct[0] == '1': # 基本移动模式
        if instruct[1] == 'mode': # 进入该模式
            os.system("gnome-terminal -e 'bash -c \"rosrun manual_control manual_ctrl\"'")
        elif instruct[1] == 'forward': # 前进
            v = virtkey.virtkey() # 调用系统键盘
            v.press_unicode(ord('w')) # 模拟字母w
            v.release_unicode(ord('w'))
            time.sleep(1)
        elif instruct[1] == 'backward': # 后退
            v = virtkey.virtkey()
            v.press_unicode(ord('s')) # 模拟字母s
            v.release_unicode(ord('s'))
            time.sleep(1)
        elif instruct[1] == 'left': # 左移
            v = virtkey.virtkey()
            v.press_unicode(ord('a')) # 模拟字母a
            v.release_unicode(ord('a'))
            time.sleep(1)
        elif instruct[1] == 'right': # 右移
            v = virtkey.virtkey()
            v.press_unicode(ord('d')) # 模拟字母d
            v.release_unicode(ord('d'))
            time.sleep(1)
        elif instruct[1] == 'stop': # 停止
            v = virtkey.virtkey()
            v.press_unicode(ord(' ')) # 模拟空格键
            v.release_unicode(ord(' '))
            time.sleep(1)
        elif instruct[1] == 'exit': # 退出此模式
            v = virtkey.virtkey()
            v.press_keysym(65307) # 模拟Esc建
            v.release_keysym(65307)
            time.sleep(1)
            os.system("exit")
    elif instruct[0] == '2': # 建立环境地图
        if instruct[1] == 'mode': # 进入该模式
            os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_gmapping.launch\"'")
            time.sleep(3)
            os.system("gnome-terminal -e 'bash -c \"rosrun manual_control manual_ctrl\"'")
        elif instruct[1] == 'forward': # 前进
            v = virtkey.virtkey() # 调用系统键盘
            v.press_unicode(ord('w')) # 模拟字母w
            v.release_unicode(ord('w'))
            time.sleep(1)
        elif instruct[1] == 'backward': # 后退
            v = virtkey.virtkey()
            v.press_unicode(ord('s')) # 模拟字母s
            v.release_unicode(ord('s'))
            time.sleep(1)
        elif instruct[1] == 'left': # 左移
            v = virtkey.virtkey()
            v.press_unicode(ord('a')) # 模拟字母a
            v.release_unicode(ord('a'))
            time.sleep(1)
        elif instruct[1] == 'right': # 右移
            v = virtkey.virtkey()
            v.press_unicode(ord('d')) # 模拟字母d
            v.release_unicode(ord('d'))
            time.sleep(1)
        elif instruct[1] == 'stop': # 停止
            v = virtkey.virtkey()
            v.press_unicode(ord(' ')) # 模拟空格键
            v.release_unicode(ord(' '))
            time.sleep(1)
        elif instruct[1] == 'exit': # 保存地图
            v = virtkey.virtkey()
            v.press_unicode(ord(' ')) # 模拟空格键
            v.release_unicode(ord(' '))
            time.sleep(1)
            v.press_keysym(65307) # 模拟Esc建
            v.release_keysym(65307)
            time.sleep(3)
            os.system("rosrun map_server map_saver -f map; exit")
            os.system("gnome-terminal -e 'bash -c \"rosnode kill rviz\"'")
            os.system("exit")
            os.system("exit")
    elif instruct[0] == '3': # 导航模式
        if instruct[1] == 'mode': # 进入该模式
            os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_navigation.launch\"'")
        elif 'Destination' in instruct[1]:
            place = instruct[2]
            os.system("gnome-terminal -e 'bash -c \"rosrun waterplus_map_tools wp_nav_test " + place + "\"'")
            os.system("exit")
        elif instruct[1] == 'exit':
            os.system("gnome-terminal -e 'bash -c \"rosnode kill rviz\"'")
            os.system("exit")
            os.system("exit")


 
if __name__=="__main__":
    IP = "192.168.31.158" # 本机IP地址
    port = 40005 # 端口号
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP,port))
    s.listen(1)
    print('listen at port :',port)
    os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_simple.launch; exec bash\"'")
    conn,addr = s.accept()
    print('connected by',addr)
    
    while True:
        data = conn.recv(1024)
        data = data.decode()# 解码
        if not data:
            break
        control_shell(data)
        print('recieved message:',data)
        # send = raw_input('return:')#python27要写raw_input,python3.X可写input
        # conn.sendall(send.encode())#再编码发送
    
    
    conn.close()
    s.close()