import falcon
import json


class API:
    def on_get(self, req:falcon.Request, res: falcon.Response):
        res.status = falcon.HTTP_200
        res.body = json.dumps({"cause": "we are 1 1"})
app = falcon.API()

api = API()
app.add_route("/api", api)
