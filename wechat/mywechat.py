#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io

docs: https://github.com/liuwons/wxBot
@time: 16/8/1 下午6:15
"""
import logging
import os
import time

import requests

from wxbot import WXBot

LOG = logging.getLogger(__name__)
forword_host = os.getenv("FORWORD_HOST", "http://127.0.0.1:8080")
data_dir = os.getenv("DATA_DIR", "data")


class MyWXBot(WXBot):

    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 1 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            # self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            # self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

        try:
            res = requests.post(forword_host, json=msg)
            if res.status_code < 400 and res.text:
                self.send_msg_by_uid(res.text, msg['user']['id'])
            else:
                LOG.warning(u"send msg error %s %s", res.status_code, res.text)
        except:
            LOG.warning(u"forward msg error %s %s", msg)

    def schedule(self):
        # TODO
        #LOG.debug("schedule run")
        time.sleep(1)


if os.path.exists(data_dir) == False:
    os.makedirs(data_dir)
wechat_utils = MyWXBot()
wechat_utils.temp_pwd = data_dir

if __name__ == '__main__':
    wechat_utils.DEBUG = True
    wechat_utils.run()
