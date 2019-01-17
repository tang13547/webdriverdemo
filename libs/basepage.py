#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import * #导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys

reload(sys)
sys.setdefaultencoding('utf-8') #解决乱码问题

"""
定位方法对应参照表:
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

"""


class Drx():
    """基于原生的selenium框架做二次封装"""

    # def __init__(self,driver):
    #     self.driver = driver

    def __init__(self,browser):
        """启动浏览器参数，默认Chrome"""
        try:
            if browser == "chrome":
                self.driver = webdriver.Chrome()
            elif browser == "firefox":
                self.driver = webdriver.Firefox()
            elif browser == "ie":
                self.driver = webdriver.Ie()
            elif browser == "edge":
                self.driver = webdriver.Edge()
            elif browser == "phantomjs":
                self.driver = webdriver.PhantomJS()
            else:
                print("Not found this %s,Please enter 'firefox', 'chrome', 'ie','phantomjs' or 'edge'" %browser)
        except Exception as msg:
            print("%s" %msg)




    def get(self,url):
        """打开url,最大化浏览器窗口，判断title是否符合预期"""
        self.driver.get(url)
        #self.driver.maximize_window()

    def max_window(self):
        """最大化浏览器窗口"""
        self.driver.maximize_window()

    def is_title_contains(self,title='',timeout=10,):
        """判断title是否包含str"""
        result = self.driver.title  # 获取url的title
        try:
            WebDriverWait(self.driver,timeout).until(EC.title_contains(title))

            print(WebDriverWait(self.driver,timeout).until(EC.title_contains(title))(self.driver))
        except TimeoutException:
            print(u"Msg：url的title为：%s 不包含： %s" % (result,title))
        except Exception as msg:
            print("Error:%s" % msg)

    def is_title(self,title='',timeout=10,):
        """判断title是否等于预期"""
        result = self.driver.title #获取url的title
        try:
            WebDriverWait(self.driver,timeout).until(EC.title_is(title))
        except TimeoutException:
            print(u"Msg：url的title为：%s != %s" % (result,title))
        except Exception as msg:
            print("Error:%s" % msg)

    def find_element(self,locator,timeout=10):
        """定位元素,参数locaator是元祖类型"""
        element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator,timeout=10):
        """定位一组元素，参数locaator是元祖类型"""
        elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self,locator):
        """
        点击操作，参数locator是元祖类型
        示例：
        locator = ("id","xxx")
        driver.find_elenment(locator)
        """
        element = self.find_element(locator)
        element.click()

    def input(self,locator,text):
        """
        文本框输入，清空后再输入,text参数为输入的内容
        示例：
        locator = ("id","xxx")
        driver.find_elenment(locator,text)
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,locator,text,timeout=10):
        """判断元素是否存在text，没定位到元素返回False，定位到返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            print("没有定位到元素：" +str(locator))
            return False
        else:
            return result

    def is_text_in_value(self,locator,text,timeout=10):
        """判断元素value值，没定位到元素返回False，定位到返回判断结果布尔值"""
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,text))
        except  TimeoutException:
            print("没有定位到元素：" + str(locator))
            return False
        else:
            return result

    def is_selected(self,locator,timeout=10):
        """判断元素是否被选中,返回布尔值"""
        result = WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self,locator,selected=True,timeout=10):
        """判断某个元素的选中状态是否符合预期,selected是期望参数True/False"""
        result = WebDriverWait(self.driver,timeout).until(EC.element_located_selection_state_to_be(locator,selected))
        return result

    def is_alert_present(self,timeout=10):
        """判断页面是否有alert,存在就返回alert对象，不存在返回False"""
        result = WebDriverWait(self.driver,timeout).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        """判断元素是否可见，可见返回True，不可见返回False"""
        try:
            #result = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            flag = True
        except:
            flag = False
        return  flag
        #print result
        #return result


    def is_invisibility(self, locator, timeout=10):
        """判断元素是否可见，可见返回本身，不可见返回True,没有找到也返回True"""
        result = WebDriverWait(self.driver,timeout).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self,locator,timeout=10):
        """判断元素是否可点击，可点击返回本身，不可点击返回Fasle"""
        result = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self,locator,timeout=10):
        """判断元素是否被定位到，定位到返回element，没定位到返回False"""
        result = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self,locator):
        """鼠标悬停操作"""
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """浏览器返回操作"""
        self.driver.back()

    def forward(self):
        """浏览器前进操作"""
        self.driver.forward()

    def close(self):
        """关闭浏览器当前页操作"""
        self.driver.close()

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()

    def refresh(self):
        """浏览器刷新"""
        self.driver.refresh()

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_url(self):
        """获取url"""
        return self.driver.current_url

    def get_text(self,locator):
        """获取元素文本"""
        element = self.find_element(locator)
        return element.text

    def get_attribute(self,locator,name):
        """获取元素的属性"""
        element = self.find_element(locator)
        return element.get_attribute(name)

    def richtext_input(self,locatior1,locatior2,text):
        """
        富文本框输入
        locatior1：为iframe定位的元素
        locatior2：为富文本框的元素
        """
        self.driver.switch_to_frame(self.driver.find_element(locatior1)) #切换到iframe
        element = self.find_element(locatior2)
        element.send_keys(Keys.TAB)
        element.send_keys(text)

    def js_execute(self,js):
        """执行js"""
        return self.driver.execute_script(js)

    def  js_focus_element(self, locator):
        """聚焦元素"""
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        """滚到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚到底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def datetime_input(self,locator,time):
        """时间控件输入"""
        js = 'document.getElementById("train_date").removeAttribute("readonly");'
        self.driver.execute_script(js)
        element=self.find_element(locator)
        element.clear()
        element.send_keys(time)

    def select_by_index(self,locator,index):
        """通过索引选择"""
        element = self.driver.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        """通过value属性选择"""
        element = self.driver.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        """通过text选择"""
        element = self.driver.find_element(locator)
        Select(element).select_by_value(text)

    def save_screenshot(self,path):
        """
        截图并保存
        path：保存路径
        """
        self.driver.save_screenshot(path)


# if __name__ == "__main__":
#     """test"""
#     driver = Drx("chrome")
#     # driver.get('https://www.cnblogs.com/langping/')
#     #
#     # button_link = ('id','blog_nav_newpost')
#     # user_input = ('id','input1')
#     # pass_input = ('id','input2')
#     # login_button = ('id','signin')
#     # driver.click(button_link)
#     # driver.send_keys(user_input,'durongxuan')
#     # driver.send_keys(pass_input,'1qaz@wsx')
#     # driver.click(login_button)
#     #
#     # title_input = ('id','Editor_Edit_txbTitle')
#     # driver.send_keys(title_input,'test test test hhhh')
#     # iframe = ('id','Editor_Edit_EditorBody_ifr')
#     # text_input = ('id','tinymce')
#     # #driver.richText_input()
#     # driver.richtext_input(iframe,text_input,'test test test hhhh')
#
#     driver.get('https://www.baidu.com/')
#     #driver.richText_input()
#     driver.is_title('百度一下')
#     input_loc = ("class name","s_ipt")
#     driver.send_keys(input_loc,"python")
#     button_loc = ("id","su")
#     driver.click(button_loc)

