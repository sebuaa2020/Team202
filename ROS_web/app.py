from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import sendMessage

app = Flask(__name__)


@app.route('/')
def goto_index():
    # sendMessage.tcp_link_conn()
    return render_template('index.html')  # 直接跳转到首页


@app.route('/index')
def index():
    pattern = request.args.get('pattern')
    action = request.args.get('action')
    msg = pattern + ' ' + action
    print(msg)
    rcv_msg = sendMessage.send_msg(msg)
    print("rcv_msg:" + rcv_msg)
    return jsonify({'status': '0', 'rcv': rcv_msg})
    # return render_template('index.html', **rcv_msg)


@app.route('/help')
def goto_help():
    return render_template('help.html')


@app.route('/about_us')
def goto_about():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run()
