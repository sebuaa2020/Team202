import subprocess

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

def control():
    # subprocess.call(["source /home/moce/demo_ws/devel/setup.bash"], shell=True, executable='/bin/bash')
    command = ["rosrun  manual_control manual_ctrl"]
    ctrl = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, executable='/bin/bash')
    key = getch()
    while True:
        key = getch()
        ctrl.stdin.write(bytes(key))
        if (ord(key) == 0x1B):
            break
    ctrl.terminate()


if __name__ == "__main__":
    control()