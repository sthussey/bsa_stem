import falcon

class BasicResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hello World Again!'

app = falcon.API()

app.add_route('/basic', BasicResource())