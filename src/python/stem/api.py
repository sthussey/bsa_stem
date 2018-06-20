import falcon
import json

from . import db

def get_request_json(req):
    if req.content_type == 'application/json':
        return json.load(req.bounded_stream)
    else:
        return None

class RequirementsResource(object):
    def on_get(self, req, resp):
        mb = req.params.get('merit_badge')
        if mb:
            requirements = db.get_requirements(mb)
            if requirements:
                resp.body = json.dumps(requirements)
                resp.content_type = 'application/json'
                resp.status = falcon.HTTP_200
            else:
                resp.status = falcon.HTTP_404
                resp.body = "Merit badge %s not found." % mb
        else:
            resp.status = falcon.HTTP_400
            resp.body = "Requires parameters merit_badge"

class CompletionsResource(object):

    def on_get(self, req, resp):
        mb = req.params.get('merit_badge')
        scout = req.params.get('scout_name')
        if mb and scout:
            completions = db.get_completions(mb, scout)
            resp.body = json.dumps(completions)
            resp.content_type = 'application/json'
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_400
            resp.body = "Requires parameters merit_badge and scout_name"

    def on_post(self, req, resp):
        """
        Expect a body of the form:
          {
              "merit_badge": <merit_badge>,
              "scout_name": <scout_name>,
              "complete" : [<req_id>, <req_id>,....],
              "incomplete": [<req_id>, <req_id>,...]
          }
          ``complete`` and/or ``incomplete`` can be empty or omitted
        """
        data = get_request_json(req)
        if data and 'merit_badge' in data and 'scout_name' in data:
            complete_reqs = data.get('complete', [])
            for req in complete_reqs:
                db.update_completion(data.get('merit_badge'), data.get('scout_name'), req, 1)

            incomplete_reqs = data.get('incomplete', [])
            for req in incomplete_reqs:
                db.update_completion(data.get('merit_badge'), data.get('scout_name'), req, 0)

            completions = db.get_completions(data.get('merit_badge'), data.get('scout_name'))
            resp.body = json.dumps(completions)
            resp.content_type = 'application/json'
            resp.status = falcon.HTTP_201
        else:
            resp.status = falcon.HTTP_400
            resp.body = "Invalid request, must provide valid JSON body."