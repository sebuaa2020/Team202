# 安装及环境配置说明

## Ubuntu 16.04安装(Desktop 64-bit recommended)

(1) 网址：http://releases.ubuntu.com/16.04/；

(2) 选择"64-bit PC(AMD64) desktop image"下载镜像；

(3) 将.iso镜像文件解压到2G容量以上的U盘，用于Ubuntu安装启动；

(4) 用Ubuntu安装启动盘引导电脑启动，进入Ubiuntu系统的安装流程；

(5) 按流程提示完成Ubuntu系统的安装。


## ROS kinetic安装

(1) 设置ROS安装源，在terminal中输入如下命令：

```
sudo sh c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release sc) main" > /etc/apt/sources.list.d/ros latest.list'
```

(2) 设置ROS安装key，在terminal中输入如下命令：

```
sudo apt key adv keyserver hkp://ha.pool.sks keyserv ers.net:80 recv key 421C365BD9FF1F717815A3895523BAEEB01FA116
```

(3) 更新安装源，在terminal中输入如下命令：

```
sudo apt-get update
```

(4) 安装ROS，在terminal中输入如下命令：

```
sudo apt-get install ros-kinetic-desktop-full
```

(5) 初始化rosdep，在terminal中输入如下命令：

```
sudo rosdep init
```

```
rosdep update
```

(6) 设置ROS软件包地址，在terminal中输入如下命令：

```
echo "source /opt/ros/kinetic/setup.bash " >> ~/.bashrc
```

```
source ~/.bashrc
```

(7) 获取ROS软件包安装工具，在terminal中输入如下命令：

```
sudo apt-get install python rosinstall
```


## ROS开发空间设置

(1) 创建开发空间并初始化，在terminal中输入如下命令：

```
mkdir -p ~/catkin_ws/src
```

```
cd ~/catkin_ws/src
```

```
catkin_init_workspace
```

```
cd ~/catkin_ws
```

```
catkin_make
```

(2) 设置开发空间软件包地址，在terminal中输入如下命令：

```
echo "source /catkin_ws/devel/setup.bash " >> ~/.bashrc
```

```
source ~/.bashrc
```

## Gazebo安装(gazebo7 required)

(1) 添加安装源，在terminal中输入如下命令：

```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
```

```
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
```

(2) 更新安装源并安装gazebo7，在terminal中输入如下命令：

```
sudo apt-get update
```

```
sudo apt-get install gezebo7
```

## 安装其他依赖

### IAI-Kinect2

​	IAI-Kinect2是用于在ROS中驱动Kinect2相机的包，从https://github.com/codeiai/iai_kinect2下载源码编译安装。

### RPLIDAR ROS

​	RPLIDAR ROS是用于在ROS中驱动RP Lidar激光雷达的包，从https://github.com/robopeak/rplidar_ros下载源码编译安装。

### 启智ROS源代码依赖

​	使用启智ROS源代码需要安装相应依赖项，逐一输入如下命令或复制至脚本执行：

```
sudo apt-get -y install ros kinetic joy
sudo apt-get -y install ros kinetic hector mapping
sudo apt-get -y install ros kinetic gmapping
sudo apt-get -y install ros kinetic map server
sudo apt-get -y install ros kinetic navigation
sudo apt-get -y install ros kinetic move base
sudo apt-get -y install ros kinetic amcl
sudo apt-get -y install ros kinetic cv bridge
sudo apt-get -y install ros kinetic audio common
sudo apt-get -y install libasound2
sudo apt-get -y install ros kinetic sound play
```
