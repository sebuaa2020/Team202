import sqlite3
import time
import hashlib


def md5(pwd):
    m = hashlib.md5()
    m.update(pwd.encode("utf8"))
    return m.hexdigest()


def addQuot(s):
    return "\"" + s + "\""


class SQL_oper:
    database_name = "team202_ROS_database.db"
    __SQL_insert = """insert into {} ({}) values ({})"""

    __SQL_update = """update {} set {} where {}"""

    __SQL_delete = """delete from {} where {}"""

    __SQL_query = """select * from {} where {}"""

    def insert(self, table, attributes, values):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        sql_statement = SQL_oper.__SQL_insert.format(table, attributes, values)
        cursor.execute(sql_statement)
        db.commit()
        db.close()

    @ classmethod
    def update(cls, table, attributes, values, conditions):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        new_values = ",".join(
            list(map(lambda x, y: "{}={}".format(x, y), attributes, values)))
        sql_statement = SQL_oper.__SQL_update.format(
            table, new_values, conditions)
        cursor.execute(sql_statement)
        db.commit()
        db.close()

    @classmethod
    def delete(cls, table, conditions):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        sql_statement = SQL_oper.__SQL_delete.format(table, conditions)
        cursor.execute(sql_statement)
        db.commit()
        db.close()

    @classmethod
    def query(cls, table, conditions):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        sql_statement = SQL_oper.__SQL_query.format(table, conditions)
        try:
            cursor.execute(sql_statement)
            res = cursor.fetchone()
        except:
            res = None
        db.commit()
        db.close()
        return res


class User(SQL_oper):
    ID = 1
    TABLE_NAME = "USER_TABLE"
    ATTRIBUTES = ["USER_ID",
                  "USER_NAME",
                  "PASSWORD",
                  "AUTHORITY"]

    def __init__(self, name, password, authority=1, id=-1):
        if id == -1:
            id = User.ID
            User.ID += 1
        self.user_id = id
        self.user_name = name
        self.user_pwd = password
        self.user_authority = authority
        self.values = [str(self.user_id), addQuot(self.user_name),
                       addQuot(self.user_pwd), str(self.user_authority)]

    def __str__(self):
        return ",".join(list(map(lambda x, y: "{}:{}".format(x, y),
                                 User.ATTRIBUTES, self.values)))

    def insert(self):
        table = User.TABLE_NAME
        attributes = ",".join(User.ATTRIBUTES)
        values = ",".join(self.values)
        return super().insert(table, attributes, values)

    @ classmethod
    def update(cls, obj):
        table = User.TABLE_NAME
        condition = "{}={}".format("USER_NAME", addQuot(obj.user_name))
        return super().update(table, User.ATTRIBUTES, obj.values, condition)

    @ classmethod
    def delete(cls, name):
        table = User.TABLE_NAME
        conditions = "{}={}".format("USER_NAME", addQuot(name))
        return super().delete(table, conditions)

    @ classmethod
    def query(cls, name):
        table = User.TABLE_NAME
        conditions = "{}={}".format("USER_NAME", addQuot(name))
        res = super().query(table, conditions)
        if res == None:
            return None
        else:
            return User(res[1], res[2], res[3], res[0])


class MapPlace(SQL_oper):
    ID = 1
    TABLE_NAME = "MAP_PLACE_TABLE"
    ATTRIBUTES = ["ID",
                  "PLACE_NAME",
                  "POS_X",
                  "POS_Y",
                  "INFO"]

    def __init__(self, name, x, y, info, id=-1):
        if id == -1:
            id = MapPlace.ID
            MapPlace.ID += 1
        self.id = id
        self.place_name = name
        self.pos_x = x
        self.pos_y = y
        self.info = info
        self.values = [str(self.id), addQuot(self.place_name), str(
            self.pos_x), str(self.pos_y), addQuot(self.info)]

    @ classmethod
    def update(cls, obj):
        table = User.TABLE_NAME
        condition = "{}={}".format("PLACE_NAME", addQuot(obj.place_name))
        return super().update(table, MapPlace.ATTRIBUTES, obj.values, condition)

    @ classmethod
    def delete(cls, name):
        table = User.TABLE_NAME
        conditions = "{}={}".format("PLACE_NAME", addQuot(name))
        return super().delete(table, conditions)

    @ classmethod
    def query(cls, name):
        table = User.TABLE_NAME
        conditions = "{}={}".format("PLACE_NAME", addQuot(name))
        res = super().query(table, conditions)
        if res == None:
            return None
        else:
            return MapPlace(res[1], res[2], res[3], res[4], res[0])


class CatchingObject(SQL_oper):
    ID = 1
    TABLE_NAME = "CATCHING_TABLE"
    ATTRIBUTES = ["ID",
                  "LABEL"
                  "POS_X",
                  "POS_Y",
                  "POS_Z",
                  "IMAGE_ROUTE"]

    def __init__(self, label, x, y, z, route="", id=-1):
        if id == -1:
            id = CatchingObject.ID
            CatchingObject.ID += 1
        self.id = id
        self.label = label
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.image_route = route
        self.values = [str(self.id), addQuot(self.label), str(self.pos_x), str(
            self.pos_y), str(self.pos_z), addQuot(self.image_route)]

    def insert(self):
        table = CatchingObject.TABLE_NAME
        attributes = ",".join(CatchingObject.ATTRIBUTES)
        values = ",".join(self.values)
        return super().insert(table, attributes, values)

    @ classmethod
    def update(cls, obj):
        table = User.TABLE_NAME
        condition = "{}={}".format("LABEL", addQuot(obj.label))
        return super().update(table, CatchingObject.ATTRIBUTES, obj.values, condition)

    @ classmethod
    def delete(cls, name):
        table = User.TABLE_NAME
        conditions = "{}={}".format("USER_NAME", addQuot(name))
        return super().delete(table, conditions)

    @ classmethod
    def query(cls, name):
        table = User.TABLE_NAME
        conditions = "{}={}".format("USER_NAME", addQuot(name))
        res = super().query(table, conditions)
        if res == None:
            return None
        else:
            return CatchingObject(res[1], res[2], res[3], res[4], res[5], res[0])

# 日志数据库供开发人员查看，所以没有查询、修改和删除的操作


class LogInfo(SQL_oper):
    ID = 1
    TABLE_NAME = "LOG_Table"
    ATTRIBUTES = ["ID",
                  "CREATE_TIME",
                  "INFO"]

    def __init__(self, info):
        self.id = LogInfo.ID
        LogInfo.ID += 1
        self.info = info
        self.time = int(time.time())
        self.values = [str(self.id), str(self.time), addQuot(self.info)]

    def insert(self):
        table = LogInfo.TABLE_NAME
        attributes = ",".join(LogInfo.ATTRIBUTES)
        values = ",".join(self.values)
        return super().insert(table, attributes, values)
