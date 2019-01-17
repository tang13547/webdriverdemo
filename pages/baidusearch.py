#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.basetestcase import Browser
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class Baidu(Browser):

    input_text = ('id','kw')
    button_click = ('id','su')

    def search(self,text):
        '''百度搜索'''
        self.driver.input\
        (self.input_text,text)#输入搜索的内容
        self.driver.click(self.button_click)#点击搜索按钮
        time.sleep(1)
        self.assertEquals(text+u'_百度搜索', self.driver.get_title())




