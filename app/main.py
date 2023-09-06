import json

import falcon
from pyrfc import Connection


class HealthResource:
    def on_get(self, request, response):
        """Handles GET requests"""
        response.status = falcon.HTTP_200
        response.text = json.dumps({"health": "OK"}, ensure_ascii=False)


class RFCResource:
    def on_get(self, request, response):
        """Handles GET requests"""
        with Connection(
            ashost="10.0.0.1", sysnr="00", client="100", user="me", passwd="secret"
        ) as conn:
            print(conn)
        response.status = falcon.HTTP_200
        response.text = json.dumps({}, ensure_ascii=False)


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()
app.add_route("/health", HealthResource())
