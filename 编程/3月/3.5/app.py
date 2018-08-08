__author__ = "Narwhale"

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(123)
        u = self.get_argument('user')
        passwd= self.get_argument('passwd')
        if u == 'hsj' and passwd == '1111':
            self.write("OK")
        else:
            self.write("GET登陆失败")

    def post(self):
        print(111)
        u = self.get_argument('user')
        passwd= self.get_argument('passwd')
        if u == 'hsj' and passwd == '1111':
            self.write("OK")
        else:
            self.write("POST 登陆失败")




application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()