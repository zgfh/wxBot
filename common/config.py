#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/7/12 下午3:49
"""
import os
def str2bool(v):
    if v is None:
        return v
    return v.lower() in ("yes", "true", "t", "1")


PROD = str2bool(os.getenv('PROD', "False"))  # 开启线上环境，减少日志，禁止DEBUG


APP_SENTRY_KEY=os.getenv('APP_SENTRY_KEY','')

APP_BASE_URL=os.getenv('APP_BASE_URL','http://127.0.0.1:5000')

if __name__ == '__main__':
    pass