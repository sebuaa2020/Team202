import socket
import sys

IP = '192.168.31.158'  # Server端的IP地址
port = 40005  # 端口号与Server端一致
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def tcp_link_conn():
    try:
        client.connect((IP, port))
        print('connect successfully!')
    except:
        print('server not find or not open')
        sys.exit()


def send_msg(message):
    client.sendall(message.encode())
    data = client.recv(1024)
    data = data.decode()
    print('received:', data)
    return data


def tcp_link_close():
    client.close()
