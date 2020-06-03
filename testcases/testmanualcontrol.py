import subprocess
import time
import multiprocessing as mp
import subprocess
import sys
import os

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    # print(ord(ch))
    return ch

# sourceIns = "source /home/moce/demo_ws/devel/setup.bash"
# command = [sourceIns, "rosrun  manual_control manual_ctrl"]
# ctrl = subprocess.Popen(command, stdin=wsubprocess.PIPE, 
#     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
#     shell=True, executable='/bin/bash', universal_newlines=True)

def testcontrol():
    def forward(v):
        v.press_unicode(ord('w'))
        v.release_unicode(ord('w'))
        time.sleep(1)
    def backward(v):
        v.press_unicode(ord('s'))
        v.release_unicode(ord('s'))
        time.sleep(1)
    def left(v):
        v.press_unicode(ord('a'))
        v.release_unicode(ord('a'))
        time.sleep(1)
    def right(v):
        v.press_unicode(ord('d'))
        v.release_unicode(ord('d'))
        time.sleep(1)
    def turnleft(v):
        v.press_unicode(ord('q'))
        v.release_unicode(ord('q'))
        time.sleep(1)
    def turnright(v):
        v.press_unicode(ord('e'))
        v.release_unicode(ord('e'))
        time.sleep(1)
    def stop(v):
        v.press_unicode(ord(' '))
        v.release_unicode(ord(' '))
        time.sleep(1)
    def esc(v):
        v.press_unicode(0x1B)
        v.release_unicode(0x1B)
        time.sleep(1)
    os.system("""gnome-terminal -e 'bash -c \"source /home/moce/demo_ws/devel/setup.bash; rosrun manual_control manual_ctrl; exec bash\"'""")
    import virtkey
    v = virtkey.virtkey()
    time.sleep(1)
    for i in range(5):
        forward(v)
    time.sleep(5)
    stop(v)
    for i in range(5):
        backward(v)
    time.sleep(5)
    stop(v)
    for i in range(5):
        left(v)
    stop(v)
    for i in range(5):
        right(v)
    time.sleep(5)
    stop(v)
    for i in range(5):
        turnleft(v)
    time.sleep(5)
    stop(v)
    for i in range(5):
        turnright(v)
    time.sleep(5)
    esc(v)
    # key = getch()
    # while True:
    #     key = getch()
    #     print(key)
    #     ctrl.stdin.write(str(key.encode("utf-8"))+'\n')
    #     ctrl.stdin.flush()
    #     # output = ctrl.communicate(input=key)
    #     # print(output)
    #     if (ord(key) == 0x1B):
    #         break
    # ctrl.terminate()


if __name__ == "__main__":
    testcontrol()