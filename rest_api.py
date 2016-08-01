#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/8/1 下午6:28
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/4/7 下午7:40
"""
import logging

import common.api_errors as api_errors
LOG = logging.getLogger(__name__)

from flask import Flask, request,url_for
from flask_restful import Resource, Api

import common.config as config

import threading
from wechat.mywechat import wechat_utils


app = Flask('wxbox')



api = Api(app)


@app.errorhandler(404)
def api_not_found(e):
    return api_errors.error_message('api_not_found', 'not found'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return api_errors.error_message('internal_server_error', 'internal server error'), 500


@app.errorhandler(api_errors.APIException)
def error_response(e):
    return api_errors.error_message(e.error_id, e.raw_message), e.code




class home(Resource):
    def get(self):
        return {'app': 'wxbox'}, 200

    def post(self):
        self.get(self)


class users(Resource):
    def get(self):
        user = request.args.get('user', None)
        LOG.debug("select user with [{}]".format(user))
        result={"contacts":wechat_utils.contact_list,"groups":wechat_utils.group_list}
        return result, 200

class messages(Resource):
    def get(self):
        return {"result":"TODO"}, 200
        pass

    def post(self):
        data_json = request.json
        LOG.debug("send message data: {}".format(data_json))
        user_name = None
        message = None
        if data_json and 'user_name' in data_json:
            user_name = data_json['user_name']
        else:
            return {"result": "send message err, can not find param:user_name ", "code": 400}, 400

        if 'message' in data_json:
            message = data_json['message']
        else:
            return {"result": "send message err, can not find param:message ", "code": 400}, 400

        wechat_utils.send_msg(user_name,message)
        return {"result":"success"}, 201

@app.route('/login_qr')
def login():
    return url_for('static', filename='qr.png')

api.add_resource(home, '/')
api.add_resource(users, '/users')
api.add_resource(messages, '/messages')

def api_run():
    app.run(host='0.0.0.0', debug=False)

def run_api_backend():
    t= threading.Thread(target=api_run)
    t.setDaemon(True)
    t.start()


def run():
    run_api_backend()
    wechat_utils.conf['qr'] = config.LOGIN_PIC
    wechat_utils.run()

if __name__ == '__main__':
    LOG.setLevel(logging.DEBUG)
    run()