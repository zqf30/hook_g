from flask import Flask, g, render_template, request, session, redirect, url_for
from utils import login_log
import os


app = Flask(__name__)
# 设置密钥
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        print('登录')
        return render_template('login.html')
    else:

        # 打印获取的`form data`内容
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')

        # 如果密码正确， 设置session并且返回成功消息
        if username == 'zqf' and password == 'zqf666':
            session['username'] = username
            g.username = username
            login_log()
            return u'登录成功！'

        # 不正确返回错误消息
        else:
            return '账号或密码错误'


@app.route('/edit/')
# 模拟编辑页面
def main_text():
    if hasattr(g, 'username'):
        return render_template('edit_user.html')
    else:
        return redirect(url_for('login'))


@app.before_request
# 判断用户是否登录，若登录则把username保存在g中
def check_session():
    if session.get('username'):
        g.username = session.get('username')


@app.context_processor
# 设置jinja2模块中的username
def username():
    if session.get('username'):
        # 判断用户是否登录
        return {"username": session.get('username')}
    else:
        # 就算不做任何操作，也要返回一个空字典
        return {}


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port='8888',
            debug=True)
