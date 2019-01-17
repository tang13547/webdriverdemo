#!coding:utf-8

import os
from libs import filepath
from xml.dom import minidom

xml_path = filepath.dataDirs('data')

# def getXmlData(value):
#     #打开xml文档
#     xml = minidom.parse(xml_path+"\\config.xml")
#     #xml = minidom.parse( "E:\\learn\\PycharmProjects\\drxtest\\data\\config.xml")
#
#     #获取根节点
#     root=xml.documentElement
#     name = root.getElementsByTagName(value)
#
#     nameValue = name[0]
#     print nameValue
#     return nameValue.firstChild.data

def getXmlData(parent,child):
    dom = minidom.parse(xml_path+ "\\config.xml")
    #dom = minidom.parse("E:\\learn\\PycharmProjects\\drxtest\\data\\config.xml")
    db = dom.documentElement
    itemlist=db.getElementsByTagName(parent)
    item = itemlist[0]
    return item.getAttribute(child)


if __name__ == "__main__":
    print getXmlData('test')
    print getXmlData('failLogin3','expected')






