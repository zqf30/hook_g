# encoding:utf-8
from flask import g


# 模拟登录日志
def login_log():
    # 模拟保存用户的用户名
    print(g.username,'已被记录')