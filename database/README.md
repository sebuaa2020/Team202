## 数据库

### 设计目标

为ROS机器人设计的数据库，供前端和后端使用，包括用户的记录、导航点的记录和运行日志记录等功能。

### 用的什么数据库

Python 自带的`sqlite3`数据库，优点有调用简单，方便快捷；缺点是可能性能不足以应对大型数据库。

### 具体代码

#### createtable.py

创建数据库表的部分，运行一次即可

#### dbmessage.py

数据库操作相关的类。其中共有四个类，分别对应四个表。

这四个类继承自同一个父类`SQL_oper`，该父类抽象对数据库各个功能的操作方法和访问接口，如查询、插入、删除、修改等，供不同子类调用达到根据不同的表项操作数据库的方法。

##### 使用方式（以User表为例）

```python
# 函数原型
class User:
    def insert(self):
        pass
    @ classmethod
    def update(cls, obj):
        pass
    @ classmethod
    def delete(cls, name):
        pass
    @ classmethod
    def query(cls, name):
        pass
# 插入数据项
new_user = User("admin", "123456", authority=1)
new_user.insert()
# 查询数据项
user = User.query("admin")
# 删除数据项
User.delete("admin")
# 更新数据项
user = User.query("admin")
user.user_pwd = "......"
User.update(user)
```

#### testdatabase.py

对数据库的单元测试，测试各个功能的正确性。

**已迁移至testcases文件夹**

## 需要完善的部分

1. 使用的数据库是Python自带的`sqlite3`，扩展性和性能方面存在一些问题，后期考虑升级使用MySQL；
2. 用户表的设计比较简单，不能满足一些复杂的需求，例如更改用户名等，需要进行扩充；
3. 主要供前端调用，与后端的交互设计不完善，没有达成最早的设计目标。

2020/6/5

