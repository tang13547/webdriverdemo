#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
import os
import HTMLTestRunner

#测试用例路径
case_path = os.path.join(os.getcwd(),"testcase")
print case_path
#报告路径
report_path = os.path.join(os.getcwd(),"report")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="login*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":

    report_abspath = os.path.join(report_path,"result.html")
    fp = open(report_abspath,"wb")
    #fp = open("E:\\learn\\PycharmProjects\\drxtest\\report\\result.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"测试报告",
                                           description=u'测试用例执行情况')

    #runner = unittest.TextTestRunner()
    runner.run(all_case())
    fp.close()