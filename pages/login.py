#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.basetestcase import Browser
from PIL import Image
from pytesseract import pytesseract
import sys,re
from libs.filepath import dataDirs
from resul import test_data_xml
import time



# 二值化  
threshold=140
table=[]
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)

#对于识别成字母的 采用该表进行修正  
rep={'O':'0', 'I':'1','L':'1', 'Z':'2', 'S':'8'}

picture_path = dataDirs('codepicture')
class Login(Browser):

    codeelement = ("id", "valicodeImg")
    username_input = ('id','username')
    password_input = ('id','password')
    code_input = ('id','vcode')
    login_button = ('xpath','//*[@id="login_form"]/div/div[2]/div[3]/button')
    username_element = ('xpath', '//*[@id="ng-app"]/body/div[2]/div[1]/div/div[1]/div[2]/span[2]')  # 登录成后的用户名

    def getVerify(self):
        '''处理图片验证码'''
        im = Image.open(picture_path+'\\code.png')#打开图片 
        imgry=im.convert('L')#图像加强
        imgry.save(picture_path+'\\code.png')
        out=imgry.point(table,'1')#二值化
        out.save(picture_path+'\\code.png')
        text=pytesseract.image_to_string(out)#识别验证码
        text=text.strip()#去除头尾的空格
        text=text.upper()#将字符串中的小写字母转换为大写
        for r in rep:
            text=text.replace(r,rep[r]) #将某些识别成字母，替换成数字
        text=str(text)
        text=re.sub("\D", "", text)#去除除数字以外的其他字符
        return text
        # print text



    def getVerifyImage(self):
        '''截图取验证码图片'''
        self.driver.save_screenshot(picture_path+"\\longin.png") #截取当前网页，该网页有我们需要的验证码
        imgelement = self.driver.find_element(self.codeelement)#定位验证码
        location = imgelement.location #获取验证码x,y轴坐标
        size = imgelement.size #获取验证码的长宽
        rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
        image = Image.open(picture_path+"\\longin.png") #打开截图
        frame4 = image.crop(rangle) #使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(picture_path+'\\code.png')  #保存截图
        verify=self.getVerify()
        return verify


    def login(self,username,password):
        '''登录'''
        while True:
            verify = self.getVerifyImage()
            #print verify
            self.driver.input(self.username_input,username)
            self.driver.input(self.password_input,password)
            self.driver.input(self.code_input,verify)
            self.driver.click(self.login_button)

            # 判断登录成后的用户名是否可见，如果不可见，说明登录失败
            if self.driver.is_visibility(self.username_element) is True:
                break
            self.driver.refresh()




