#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/3/5 上午9:33
"""
import logging

import config

log_level=logging.DEBUG
if config.PROD:
    log_level=logging.INFO

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=log_level)
logging.getLogger(__name__).info('log init prod')



if __name__ == '__main__':
    pass