# flask入门项目

学习这个[教程](https://helloflask.com/book/3/)

最终实现了一个基于flask的[简单web页面](http://plala.pythonanywhere.com)

前置知识：

- web前端开发（html,css,js）
- 懂点python

耗时：

- 大概两天左右

## flask介绍：

[flask官方文档](https://flask.palletsprojects.com/en/3.0.x/)

Flask 是一个轻量级[WSGI](https://wsgi.readthedocs.io/) Web 应用程序框架。它旨在让入门变得快速、简单，并且能够扩展到复杂的应用程序。它最初是[Werkzeug](https://werkzeug.palletsprojects.com/) 和[Jinja](https://jinja.palletsprojects.com/)的简单包装，现已成为最流行的 Python Web 应用程序框架之一。

Flask 提供建议，但不强制执行任何依赖项或项目布局。由开发人员选择他们想要使用的工具和库。社区提供了许多扩展，可以轻松添加新功能。

## attention

使用windows开发需要注意以下几点：

- 在 CMD.exe 中使用 `dir` 命令替代 `ls` 命令，使用 `type` 命令替代 `cat` 命令

- 创建文件

  ```c
  type nul > filename
  ```

- 命令提示符里跳转到D盘时输入 `D:` 再cd

**所有命令均需要在激活虚拟环境后执行**

```
$ env\Scripts\activate  # Windows 激活虚拟环境
 env\Scripts\deactivate  #退出虚拟环境 CMD下
```



## 第一节 准备工作

### 配置git

按照教程即可

### 创建虚拟环境

遇到了以下问题：报错了但是创建成功了

命令如下（因为之前有需求同时用到py2和py3，所以改了python命令为python2和python3）

```
$ python3 -m venv env
Error: [WinError 2] ϵͳ▒Ҳ▒▒▒ָ▒▒▒▒▒ļ▒▒▒
```

看目录似乎创建成功了，但是查了下发现Scripts文件夹里为空，创建失败。

检查了python配置的环境变量和版本，好像都没问题

**解决方案：**

在同学的电脑上配置了env发给了自己，运行成功

得到了python3.10的虚拟环境

### 安装flask

注意[更换pip源](https://zhuanlan.zhihu.com/p/57872888)



## 第二节 

Flask 是典型的微框架，作为 Web 框架来说，它仅保留了核心功能：**请求响应处理**和**模板渲染**。

### 主页

执行`flask run`

默认路径为[http://localhost:5000](http://localhost:5000/) 

### 程序发现机制

Flask 默认会假设你把程序存储在名为 app.py 或 wsgi.py 的文件中，使用其他名称要更改系统变量：

将app.py改为hello.py

在cmd中输入:

```
set FLASK_APP=hello.py
flask run
```

### 环境变量

- FLASK_APP用来设置要运行的程序实例
- FLASK_DEBUG 用来开启调试模式（debug mode）。调试模式开启后，当程序出错，浏览器页面上会显示错误信息；代码出现变动后，程序会自动重载。

### 实验

- 视图函数的返回值默认会被浏览器作为 HTML 格式解析
- 一个视图函数也可以绑定多个 URL
- 安全： 用户输入的数据会包含恶意代码，使用escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;。这样在返回响应时浏览器就不会把它们当做代码执行

### 问题

**git push 失败**

解决方案：改端口号

```
//git端口号与本地不一致
git config --global http.proxy 
```

## 第三节 模板 渲染

- **模板：**包含变量和运算逻辑的 HTML 或其他格式的文本
- **渲染：**执行这些变量替换和逻辑计算工作的过程

### [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/templates)  模板渲染引擎

语法和 Python 大致相同，后面会陆续接触到一些常见的用法。在模板里，需要添加特定的定界符将 Jinja2 语句和变量标记出来，下面是三种常用的定界符：

- `{{ ... }}` 用来标记变量。
- `{% ... %}` 用来标记语句，比如 if 语句，for 语句等。
- `{# ... #}` 用来写注释。

模板中使用的变量需要在渲染的时候传递进去。

### [Faker](https://github.com/joke2k/faker)

- 使用 [Faker](https://github.com/joke2k/faker) 可以实现自动生成虚拟数据，它支持丰富的数据类型，比如时间、人名、地名、随机字符等。
- 感觉可以用来生成测试数据

## 第四节 静态文件

### url_for()

文件的 URL 可以通过 Flask 提供的 `url_for()` 函数来生成.

传入端点值（视图函数的名称）和参数，它会返回对应的 URL。

```
<img src="{{ url_for('static', filename='foo.jpg') }}">
```

### 添加静态文件

- 可以借助前端框架来完善页面样式，比如 [Bootstrap](https://getbootstrap.com/)、[Semantic-UI](http://semantic-ui.com/)、[Foundation](https://foundation.zurb.com/) 等。它们提供了大量的 CSS 定义和动态效果，使用起来非常简单。
- 扩展 [Bootstrap-Flask](https://github.com/helloflask/bootstrap-flask) 可以简化在 Flask 项目里使用 Bootstrap 的步骤。

## 第五节 数据库

选择[SQLite](https://www.sqlite.org/)，它基于文件，不需要单独启动数据库服务器，适合在开发时使用，或是在数据库操作简单、访问量低的程序中使用。

###  [SQLAlchemy](https://www.sqlalchemy.org/)

通过定义 Python 类来表示数据库里的一张表（类属性表示表中的字段 / 列），通过对这个类进行各种操作来代替写 SQL 语句。这个类我们称之为**模型类**，类中的属性我们将称之为**字段**。

```
打开 Python Shell 使用的是 flask shell命令，而不是 python。使用这个命令启动的 Python Shell 激活了“程序上下文”，它包含一些特殊变量，这对于某些操作是必须的（比如上面的 db.create_all()调用）。请记住，后续的 Python Shell 都会使用这个命令打开。
```

- `app.root_path` 返回程序实例所在模块的路径
- 打开 Python Shell 使用的是 `flask shell`命令，在其中运行对数据库操作的命令

### **自定义命令**

- flask initdb：初始化数据库，--drop为先清空再初始化

- flask forge：向数据库中添加虚拟数据

## 第六节 模板优化

### 自定义错误界面：

实现了400、404、405

### 模板上下文处理函数

解决重复变量传参：

```python
@app.context_processor #装饰器
def inject_user():  # 函数名可以随意修改
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于 return {'user': user}
```

返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以直接在模板中使用。

### 使用模板继承组织模板

解决模板内容重复：

利用Jinja2，定义父模板作为基模板，用extends来继承

基模板中需要在实际的子模板中追加或重写的部分则可以定义成

块（block）。块使用 `block` 标签创建，`{% block 块名称 %}` 作为开始标记，`{% endblock %}` 或 `{% endblock 块名称 %}` 作为结束标记。

子模板中，默认的块重写行为是覆盖，想追加用super(),即 `{{ super() }}`



## 第七节 表单

### 处理数据

`flash`实现消息提示框，使用flash需要在基模板中添加提示消息

post时需要设置flask的随机密钥：

```python
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'
```

### 表单校验

建议使用第三方库（比如 [WTForms](https://github.com/wtforms/wtforms)）来实现表单数据的验证工作。

```
可以自动生成表单对应的 HTML 代码，并在表单提交时验证表单数据，返回对应的错误消息。内置了 CSRF（跨站请求伪造） 保护功能。
```

扩展 [Bootstrap-Flask](https://github.com/helloflask/bootstrap-flask) 

避免CSRF攻击：比对coockie

## 第八节 用户认证

### 安全储存密码

Flask 的依赖 Werkzeug 内置了用于生成和验证密码散列值的函数，`werkzeug.security.generate_password_hash()` 用来为给定的密码生成密码散列值，而 `werkzeug.security.check_password_hash()` 则用来检查给定的散列值和密码是否对应

### 管理员

只在后台生成，前端无注册界面

### 用户认证

通过[Flask-Login](https://github.com/maxcountryman/flask-login) 实现登录登出

### 认证保护

在 Web 程序中，有些页面或 URL 不允许未登录的用户访问，而页面上有些内容则需要对未登陆的用户隐藏，这就是认证保护。（用户权限）

## 第九节 测试

自动化测试：应该在开发每一个功能后立刻编写相应的测试，确保测试通过后再开发下一个功能。

### 单元测试

用 Python 标准库中的测试框架 unittest 来编写单元测试

- 测试视图函数

- 测试自定义命令

  ​	`app.test_cli_runner()` 方法返回一个命令运行器对象，我们创建类属性 `self.runner` 来保存它。通过对它调用 `invoke()` 方法可以执行命令，传入命令函数对象，或是使用 `args` 关键字直接给出命令参数列表。`invoke()` 方法返回的命令执行结果对象，它的 `output` 属性返回命令的输出信息。

### 测试覆盖率

如何才能知道程序里有哪些代码还没有被测试？整体的测试覆盖率情况如何？使用 [Coverage.py](https://coverage.readthedocs.io/en/v4.5.x/) 来检查测试覆盖率。

或者 [pytest](https://pytest.org/)

结果如下：

```
>  coverage report
Name     Stmts   Miss  Cover
----------------------------
app.py     174     13    93%
----------------------------
TOTAL      174     13    93%
```



## 第十节 组织代码

总的来说就是把之前混乱的代码改为包结构

（应该从一开始开发的时候就采用啊）

- [蓝本](https://flask.palletsprojects.com/blueprints/)类似于子程序的概念，借助蓝本你可以把程序不同部分的代码分离开（比如按照功能划分为用户认证、管理后台等多个部分），即对程序进行模块化处理。
- [工厂函数](https://flask.palletsprojects.com/patterns/appfactories/)就是创建程序的函数。在工厂函数内，我们先创建程序实例，并在函数内完成初始化扩展、注册视图函数等一系列操作，最后返回可以直接运行的程序实例。

## 第十一节

### PythonAnywhere 

- 发布时注意自己的python版本

- 注意每三个月的链接

nano的保存并退出命令：

```
//ctrl+o enter 保存
//ctrl+x 退出
```

更新部署后程序：

```
$ cd watchlist
$ git pull
```

