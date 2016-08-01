#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io

docs: https://github.com/liuwons/wxBot
@time: 16/8/1 下午6:15
"""

import time
from wxbot import *

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
        #TODO
    def schedule(self):
        self.send_msg(u'tb', u'schedule')
        time.sleep(1)



wechat_utils = MyWXBot()

if __name__ == '__main__':
    wechat_utils.DEBUG = True
    wechat_utils.run()
