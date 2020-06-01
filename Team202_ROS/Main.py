import socket
import threading
import os
import time
import subprocess


def str2shell(str):
    if str == 'map_start':
        os.system("source ./devel/setup.bash; roslaunch wpr_simulation wpb_gmapping.launch")
    if str == 'map_finish':
        os.system("source ./devel/setup.bash; rosrun map_server map_saver -f map;cp ./map.pgm ./src/wpr_simulation/maps;cp ./map.yaml ./src/wpr_simulation/maps;")
    
    if str == 'move_forward':
        os.system("source ./devel/setup.bash;roslaunch wpr_simulation wpb_rviz.launch;source ./devel/setup.bash;rosrun wpr_simulation go_forward")
    if str == 'move_backward':
        os.system("source ./devel/setup.bash;roslaunch wpr_simulation wpb_rviz.launch;source ./devel/setup.bash;rosrun wpr_simulation go_backward")
    if str == 'move_left':
        os.system("source ./devel/setup.bash;roslaunch wpr_simulation wpb_rviz.launch;source ./devel/setup.bash;rosrun wpr_simulation go_left")
    if str == 'move_right':
        os.system("source ./devel/setup.bash;roslaunch wpr_simulation wpb_rviz.launch;source ./devel/setup.bash;rosrun wpr_simulation go_right")

    if str == 'navigation':
        os.system("source ./devel/setup.bash;roslaunch wpr_simulation wpb_navigation.launch")

    if str == 'move':
        os.system("source ./devel/setup.bash;roslaunch wpr_simulation wpb_rviz.launch;source ./devel/setup.bash; rosrun wpr_simulation keyboard_vel_ctrl")

def tcplink():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    winip = '192.168.43.6'
    linuxip = '192.168.43.229'
    s.bind((linuxip, 9999))
    s.listen(1)
    while True:
        print('waiting for connection.....')
        sock, addr = s.accept()
        print('Accept new connection from %s:%s...' % addr)
        try:
            data = sock.recv(1024)
            rcvStr = data.decode('utf-8')
            if (rcvStr == 'end'):
                sock.close()
                break
            sendStr = 'received: ' + rcvStr + '\r\n'
            str2shell(rcvStr)
            sock.send(sendStr.encode('utf-8'))
            print(sendStr.replace('\r\n', ''))
            sock.close()
        except ConnectionAbortedError as e:
            print('Connection Aborted!')
        finally:
            print('Connection from %s:%s closed.' % addr)
    s.shutdown(2)
    s.close()

tcplink()

if __name__=="__main__":
    str2shell('map_start')