#!/usr/bin/env python
#-*- coding:utf-8 -*-+

import os

def dataDirs(path):
    '''文件目录获取,path参数为当前项目的某个包名'''
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIRS = (os.path.join(BASE_DIR),path)
    d = '\\'.join(DATA_DIRS)
    return d
