# coding=utf8
from __future__ import unicode_literals

import json
import datetime
from flask import Response

class APIException(Exception):
    skip_sentry = True

    def __init__(self, error_id, message, code=500):
        super(APIException, self).__init__()
        self.raw_message = message
        self.error_id = error_id
        self.code = code
        # cause python & celery only dump message to error info,
        # we use raw_message to save message, and message field to save APIException info
        self.message = json.dumps(dict(error_id=error_id, message=str(message), code=code))


def datetime_handler(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return obj.isoformat()
    else:
        return None

def json_resp(obj, headers=None):
    return Response(json.dumps(obj, indent=4, default=datetime_handler), mimetype='application/json', headers=headers)


def error_message(error_id, message):
    return json_resp({'error_id': error_id, 'message': message})

