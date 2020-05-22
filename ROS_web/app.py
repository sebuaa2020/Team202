from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def goto_index():
    return render_template('index.html')  # 直接跳转到首页


@app.route('/index')
def index():
    pattern = request.args.get('pattern')
    action = request.args.get('action')
    print(pattern)
    print(action)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
