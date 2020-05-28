from dbmessage import md5, User, LogInfo

if __name__ == "__main__":
    print("INSERT")
    res = User.query("admin")
    if res == None:
        user = User("admin", md5("123456"))
        user.insert()
        res = User.query("admin")
        assert res != None
        print("insert PASS")

    print("QUERY")
    print("query existing user")
    res = User.query("admin")
    assert res != None
    assert res.user_pwd == md5("123456")
    print("query non-existent user PASS")
    print("query non-existent user")
    res = User.query("T222")
    assert res == None
    print("query non-existent user PASS")
    print("query PASS")

    print("UPDATE")
    User.update(User("admin", md5("T202")))
    res = User.query("admin")
    assert res.user_pwd == md5("T202")
    print("update PASS")

    print("DELETE")
    user_name = "admin"
    try:
        User.delete(user_name)
    except:
        print("user %s is not existing" %(user_name))
    res = User.query("admin")
    assert res == None
    print("delete PASS")

    res = User.query("user_1")
    if res == None:
        cbw = User("user_1", md5("cbw"), 1)
        cbw.insert()
    
    res = User.query("user_1")
    assert res != None

    print("User PASS")

    log = LogInfo("test logging db 1st.")
    log.insert()
