#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pages.baidusearch import Baidu
from libs.basetestcase import Browser
import unittest,sys
from libs import filepath
import ddt
from resul.excle import ExcelUtil

reload(sys)
sys.setdefaultencoding('utf-8')

#filePath = 'F:\\project\\workspace\\webdriverdemo\\data\\test.xlsx'
#sheetName = 'Sheet1'
filePath = filepath.dataDirs('data') + '\\test.xlsx'
data = ExcelUtil(filePath, 'Sheet1')
dataTest= data.dict_data()

@ddt.ddt
class BaiduCase(Baidu,unittest.TestCase):

    @ddt.data(*dataTest)
    def testBaiduSearch(self,data):
        '''百度搜索用例'''
        self.search(data['search'])
        #self.assertEquals(u'python_百度搜索', self.driver.get_title())


if __name__ == "__main__":
    unittest.main()