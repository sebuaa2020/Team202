from dbmessage import *
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ROS database cmd")
    parser.add_argument("-t", help="input the table name")