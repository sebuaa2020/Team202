import sqlite3
import time
# father class


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
        cursor.execute(sql=sql_statement)
        db.commit()
        db.close()

    def update(self, table, attributes, values):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        sql_statement = SQL_oper.__SQL_update.format(table, attributes, values)
        cursor.execute(sql=sql_statement)
        db.commit()
        db.close()

    def delete(self, table, conditions):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        sql_statement = SQL_oper.__SQL_delete.format(table, conditions)
        cursor.execute(sql=sql_statement)
        db.commit()
        db.close()

    def query(self, table, conditions):
        db = sqlite3.connect(database=SQL_oper.database_name)
        cursor = db.cursor()
        sql_statement = SQL_oper.__SQL_query.format(table, conditions)
        cursor.execute(sql=sql_statement)
        db.commit()
        db.close()


class User(SQL_oper):
    ID = 1
    TABLE_NAME = "USER_TABLE"
    ATTRIBUTES = ["ID",
                  "USER_NAME",
                  "PASSWORD",
                  "AUTHORITY"]

    def __init__(self, name, password, authority=1):
        self.user_id = User.ID
        User.ID += 1
        self.user_name = name
        self.user_pwd = password
        self.user_authority = authority
        self.values = [str(self.user_id), str(self.user_name),
                       str(self.user_pwd), str(self.user_authority)]

    def insert(self):
        table = User.TABLE_NAME
        attributes = ",".join(User.ATTRIBUTES)
        values = ",".join(self.values)
        return super().insert(table, attributes, values)

    # def update(self, table, attributes, values):
    #     table = User.TABLE_NAME
    #     attributes = ",".join(User.ATTRIBUTES)
    #     values = ",".join(self.values)
    #     return super().update(table, attributes, values)

    def delete(self):
        table = User.TABLE_NAME
        conditions = ",".join(
            list(map(lambda x, y: "{}:{}".format(x, y), User.ATTRIBUTES, self.values)))
        return super().delete(table, conditions)

    # def query(self, table, conditions):
    #     table = User.TABLE_NAME
    #     return super().query(table, conditions)


class MapPlace(SQL_oper):
    ID = 1
    TABLE_NAME = "MAP_PLACE_TABLE"
    ATTRIBUTES = ["ID",
                  "PLACE_NAME",
                  "CREATE_TIME",
                  "POS_X",
                  "POS_Y",
                  "INFO"]

    def __init__(self, name, x, y, info=""):
        self.id = MapPlace.ID
        MapPlace.ID += 1
        self.place_name = name
        self.time = int(time.time())
        self.pos_x = x
        self.pos_y = y
        self.info = info
        self.values = [str(self.id), str(self.place_name),
                       str(self.time), str(self.pos_x), str(self.pos_y), str(self.info)]

    def insert(self, table, attributes, values):
        table = MapPlace.TABLE_NAME
        attributes = ",".join(MapPlace.ATTRIBUTES)
        values = ",".join(self.values)
        return super().insert(table, attributes, values)

    # def update(self, table, attributes, values):
    #     table = MapPlace.TABLE_NAME
    #     return super().update(table, attributes, values)

    def delete(self):
        table = MapPlace.TABLE_NAME
        conditions = ",".join(
            list(map(lambda x, y: "{}:{}".format(x, y), MapPlace.ATTRIBUTES, self.values)))
        return super().delete(table, conditions)

    # def query(self, table, conditions):
    #     table = MapPlace.TABLE_NAME
    #     return super().query(table, conditions)


class CatchingObject(SQL_oper):
    ID = 1
    TABLE_NAME = "CATCHING_TABLE"
    ATTRIBUTES = ["ID",
                  "CREATE_TIME",
                  "POS_X",
                  "POS_Y",
                  "POS_Z",
                  "IMAGE_ROUTE"]

    def __init__(self, label, x, y, z, route=""):
        self.id = CatchingObject.ID
        CatchingObject.ID += 1
        self.time = int(time.time())
        self.image_route = route
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.image_route = route
        self.values = [str(self.id), str(self.time), str(self.pos_x), str(
            self.pos_y), str(self.pos_z), str(self.image_route)]

    def insert(self):
        table = CatchingObject.TABLE_NAME
        attributes = CatchingObject.ATTRIBUTES
        values = ",".join(self.values)
        return super().insert(table, attributes, values)

    # def update(self, table, attributes, values):
    #     table = CatchingObject.TABLE_NAME
    #     attributes = CatchingObject.ATTRIBUTES
    #     return super().update(table, attributes, values)

    def delete(self, table, conditions):
        table = CatchingObject.TABLE_NAME
        conditions = ",".join(
            list(map(lambda x, y: "{}:{}".format(x, y), CatchingObject.ATTRIBUTES, self.values)))
        return super().delete(table, conditions)

    def query(self, table, conditions):
        table = CatchingObject.TABLE_NAME
        return super().query(table, conditions)


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
        self.values = [str(self.id), str(self.time), str(self.info)]

    def insert(self):
        table = LogInfo.TABLE_NAME
        attributes = LogInfo.ATTRIBUTES
        values = ",".join(self.values)
        return super().insert(table, attributes, values)

    # def update(self, table, attributes, values):
    #     table = LogInfo.TABLE_NAME
    #     return super().update(table, attributes, values)

    def delete(self, table, conditions):
        table = LogInfo.TABLE_NAME
        conditions = ",".join(
            list(map(lambda x, y: "{}:{}".format(x, y), LogInfo.ATTRIBUTES, self.values)))
        return super().delete(table, conditions)

    # def query(self, table, conditions):
    #     table = LogInfo.TABLE_NAME
    #     return super().query(table, conditions)
