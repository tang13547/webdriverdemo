#!/usr/bin/env python
#-*- coding:utf-8 -*-

from basepage import Drx
from resul import test_data_xml
#from selenium import webdriver
import unittest



class Browser(unittest.TestCase):
    """启动浏览器基类"""

    @classmethod
    def setUpClass(cls):
        #browser = testDataXml.getXmlBrowser('driver','browser')
        #url = testDataXml.getXmlBrowser('Url','url')
        cls.driver = Drx(test_data_xml.getXmlData('Browser', 'browser'))#浏览器在config.xml中配置
        cls.driver.get(test_data_xml.getXmlData('Url', 'url')) #测试url在config.xml中配置

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
