#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pages.login import Login
from resul import test_data_xml
from resul.excle import ExcelUtil
from libs import filepath
import unittest
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

filePath = filepath.dataDirs('data') + '\\test.xlsx'
data = ExcelUtil(filePath, 'Sheet2')
logindata = data.dict_data()
# print logindata
# print logindata[0]["username"]
# print logindata[0]["password"]

username_element = ('xpath','//*[@id="ng-app"]/body/div[2]/div[1]/div/div[1]/div[2]/span[2]') #登录成后的用户名
class Ycgesm(Login,unittest.TestCase):

    def testLogin(self):
        '''登录用例'''
        #username = logindata[0]["username"] #从excel中读取的username
        #password = logindata[0]["password"] #从excel中读取的password
        username = test_data_xml.getXmlData("islogin","username")  #从xml中读取的username
        password = test_data_xml.getXmlData("islogin","password") #从xml中读取的username
        self.login(username,password)
        self.assertEqual(self.driver.get_text(username_element),test_data_xml.getXmlData("islogin","expected"))

        # print self.driver.get_text(username_element)
        # print test_data_xml.getXmlData("islogin","expected")





if __name__ == "__main__":
    unittest.main()
