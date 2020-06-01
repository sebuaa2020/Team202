from flask import Flask, redirect, session, url_for, flash
from flask import render_template
from flask import request
from flask import jsonify
import sendMessage
import dbmessage

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'  # flask生成密钥


@app.route('/')
def goto_index():
    # sendMessage.tcp_link_conn()
    return render_template('login.html')  # 直接跳转到首页


@app.route('/login')
def get_login_request():
    username = request.args.get('loginUsername')
    password = request.args.get('loginPassword')
    if username:
        result = dbmessage.User.query(username)
        if result and result.user_pwd == password:  # 用户名和密码与数据库中数据相对应
            session['name'] = username
            return redirect(url_for('index', name=username, _external=True))
        else:
            flash('用户名或密码不正确！')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/register')
def add_user():
    username = request.args.get('registerUsername')
    password = request.args.get('registerPassword')
    if username:
        result = dbmessage.User.query(username)
        if result:
            flash('邮箱已被注册！')
            return render_template('register.html')
        else:
            user = dbmessage.User(username, password)
            user.insert()
            flash('注册成功！请登录')
            return render_template('login.html')
    return render_template('register.html')


@app.route('/index')
def index():
    user_id = session.get('name')
    pattern = request.args.get('pattern')
    action = request.args.get('action')
    if action:
        msg = pattern + ' ' + action
        print(msg)
        rcv_msg = sendMessage.send_msg(msg)
        print("rcv_msg:" + rcv_msg)
        return jsonify({'status': '0', 'rcv': rcv_msg})
    else:
        return render_template('index.html')


@app.route('/help')
def goto_help():
    return render_template('help.html')


@app.route('/about_us')
def goto_about():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run()
