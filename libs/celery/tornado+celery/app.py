from tornado import web
import task 

class TestHandler(tornado.web.RequestHandler):

    @web.asynchronous
    def get(self):
        task.mytask0.apply_async(
            args=['task0'], 
            queue='mytask0',
            routing_key='task.mytask0', 
            callback=self.on_success)
    
    def on_success(self, result):
        self.finish({'task':result.result})
