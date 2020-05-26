from dbmessage import md5, User

if __name__ == "__main__":
    res = User.query("admin")
    if res == None:
        user = User("admin", md5("123456"))
        user.insert()
    User.update(User("admin", md5("T202"), 1))
    res = User.query("admin")
    assert res != None
    print(res)
    User.delete("admin")
    res = User.query("admin")
    assert res == None
    print("User pass")
