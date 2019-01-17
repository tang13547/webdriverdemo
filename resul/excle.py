#!/usr/bin/env python
#-*- coding:utf-8 -*-+

import os
import xlrd
from libs import filepath

#case_path = os.path.join(os.getcwd(),"../data")
#case_path =  os.path.abspath(os.path.join(os.getcwd(), "../data")) #读取上一级目录
case_path = filepath.dataDirs('data')

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        #  获取总行数
        self.rowNum = self.table.nrows
        #  获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r

if __name__ == "__main__":
    #filePath = 'F:\\project\\workspace\\webdriverdemo\\data\\test.xlsx'
    filePath = case_path+'\\test.xlsx'
    print filePath
    sheetName = 'Sheet1'
    data = ExcelUtil(filePath, sheetName)
    dataTset= data.dict_data()
    print dataTset[0]['search']

