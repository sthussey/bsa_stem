import falcon

from stem.api import BasicResource

app = falcon.API()

app.add_route('/basic', BasicResource())