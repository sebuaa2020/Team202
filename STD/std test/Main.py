import socket
import threading
import os
import time
import subprocess


def str2shell(str):
    if str == 'map_start':
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_gmapping.launch; exec bash\"'")
    if str == 'move_forward':
        os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation go_forward\"'")
    if str == 'move_backward':
        os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation go_backward\"'")
    if str == 'move_left':
        os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation go_left\"'")
    if str == 'move_right':
        os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation go_right\"'")
    if 'navigation' in str:
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_navigation.launch\"'")






