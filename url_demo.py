from flask import Flask, current_app, redirect, url_for

# 创建Flask的应用对象
# '__name__'表示当前的模块名
# 模块名。flask以这个模块所在的目录为总目录，默认这个目录中的static目录为静态目录，templates为模板目录
app = Flask(__name__)


@app.route("/")
def index():
    """定义的视图函数"""
    return "hello world"

def hello():
    return "hello"


@app.route("/h1")
@app.route("/h2")
def hi():
    """配置两个路径"""
    return "hi girl"


@app.route("/login")
def login():
    """url反解析"""
    # 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
    url = url_for("index")
    return redirect(url)


# 通过mwthods限定访问方式
@app.route("/post_only", methods=["POST"])
def post_only():
    return "post only page"


# 两个对象函数使用相同的域名时，如果访问方式不一样，是可以的
@app.route("/hello", methods=["POST"])
def hello1():
    return "hello 1"


@app.route("/hello2", methods=["GET"])
def hello2():
    return "hello 2"


if __name__ == '__main__':
    # 通过url_map可以查看整个项目中的路由信息
    print(app.url_map)
    # app.run()参数
    app.run(host='192.168.0.112', port=5000, debug=True)