from flask import Flask, current_app

# 创建Flask的应用对象
# '__name__'表示当前的模块名
# 模块名。flask以这个模块所在的目录为总目录，默认这个目录中的static目录为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path='/python',  # 访问静态资源的url前缀， 默认值是static
            # static_folder=''  # 静态文件目录， 默认是static
            # template_folder=''  # 模板文件目录， 默认是templates
            )

# ====》 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile("config.cfg")

# 2.使用对象配置参数
class Config(object):
    DEBUG = True
    YEAR = '2019'


app.config.from_object(Config)

# 3.直接操作config的字典对象
# app.config["DEBUG"] = True



@app.route("/index")
def hello():
    """定义的视图函数"""
    # a = 1 + '1'
    # ===>读取配置参数
    # 1.直接从全局对象app的config字典中取值
    # year = app.config.get("YEAR")

    # 2.通过current_app获取
    year = current_app.config.get('YEAR')

    return year


if __name__ == '__main__':
    # app.run()参数
    app.run(host='192.168.0.112', port=5000, debug=True)