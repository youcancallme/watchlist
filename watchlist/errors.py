from flask import render_template

from watchlist import app

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('error.html',code=404, reason='请求的资源不存在'), 404  # 返回模板和状态码

@app.errorhandler(400)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('error.html',code=400, reason='请求错误，服务器无法理解'), 400  # 返回模板和状态码

@app.errorhandler(405)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('error.html',code=405, reason='方法不允许'), 405  # 返回模板和状态码