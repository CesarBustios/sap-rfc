import json
import os

import falcon
from pyrfc import Connection


class HealthResource:
    def on_get(self, request, response):
        """Handles GET requests"""
        response.status = falcon.HTTP_200
        response.text = json.dumps({"health": "OK"}, ensure_ascii=False)


class RFCResource:
    @staticmethod
    def _get_sap_connection():
        return Connection(
            ashost=os.environ.get("SAP_ASHOST"),
            sysnr=os.environ.get("SAP_SYSNR"),
            client=os.environ.get("SAP_CLIENT"),
            user=os.environ.get("SAP_USER"),
            passwd=os.environ.get("SAP_PASSWD"),
        )

    def on_get(self, request, response):
        """Handles GET requests"""
        # Get the RFC function name and take it out of the params, any other params in
        # the request will be used for the RFC function call.
        try:
            func_name = request.params.pop("func_name")
        except KeyError as exc:
            raise falcon.HTTPBadRequest(
                title="Function name not provided.",
                description="An RFC function name must be provided.",
            ) from exc
        else:
            func_params = request.params

        with self._get_sap_connection() as conn:
            result = conn.call(func_name, **func_params)
            response.status = falcon.HTTP_200
            response.text = json.dumps({"result": result}, ensure_ascii=False)


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()
app.add_route("/health", HealthResource())
app.add_route("/rfc", RFCResource())
