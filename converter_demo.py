from flask import Flask, current_app
from werkzeug.routing import BaseConverter

# 创建Flask的应用对象
# '__name__'表示当前的模块名
# 模块名。flask以这个模块所在的目录为总目录，默认这个目录中的static目录为静态目录，templates为模板目录
app = Flask(__name__)


# 转换器
# 127.0.0.1:5000/goods/123
# @app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")  # 不加转换器类型， 默认是普通字符串规则（除了/的字符）
def goods_detail(goods_id):
    """定义的视图函数"""
    return "good_detail page %s" % goods_id

# 1.定义自己的转化器
class RegexConverter(BaseConverter):
    """实现自己的转换器"""
    def __init__(self, url_map, regex):  # url_map 是给父类用的
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会使用这个属性来进行正则表达式的正则匹配
        self.regex = regex

# 2.将自定义的转化器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter

# 3.使用自定义转换器
@app.route("/send/<re(r'1[3456789]\d{9}'):mobile>")
def send_msg(mobile):
    return "send msg to %s" % mobile


if __name__ == '__main__':
    # app.run()参数
    app.run(host='192.168.0.112', port=5000, debug=True)