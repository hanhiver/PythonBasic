import tornado.ioloop #核心io循环
import tornado.httpserver #异步非阻塞HTTP服务
import tornado.web #web框架模块
import tornado.options #解析终端参数模块

# 从终端模块中导出define用于读取参数，option用于设置默认参数。
from tornado.options import define, options 

# 定义端口用于指定HTTP服务监听端口
# 如果命令行中带有port同名参数则会成为全局tornado.options的属性，若没有则用define定义。
define("port", type=int, default=8888, help="Run on the given port.")

# 创建请求处理器。
# 当处理请求时会进行实例化并调用HTTP对应的请求方法。 
class IndexHandler(tornado.web.RequestHandler):
    
    # 定义GET方法对请求作出响应。
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若没有则为0.
        id = self.get_argument("id", "0")
        # write方法将字符串写入HTTP响应。
        self.write("hello world,  id = " + id)

# 创建路由表。
urls = [ 
    (r"/", IndexHandler),
]

def main():
    # 解析命令行参数。
    tornado.options.parse_command_line()
    # 创建应用实例。
    app = tornado.web.Application(urls, {"debug":True})
    # 获取监听端口
    app.listen(options.port)
    # 床及哦按IOLoop并启动。
    tornado.ioloop.IOLoop.current().start()

# 应用入口，解析命令行参数。 
if __name__ == '__main__':
    main()
