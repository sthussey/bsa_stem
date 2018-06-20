import falcon

from stem.api import RequirementsResource
from stem.api import CompletionsResource

app = falcon.API()

app.add_route('/requirements', RequirementsResource())
app.add_route('/completions', CompletionsResource())