import json

import falcon


class HealthResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.text = json.dumps({"health": "OK"}, ensure_ascii=False)


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()
app.add_route("/health", HealthResource())
