# -*- coding: utf-8 -*-
"""
##图片分析函数
@author: zs
"""
from printscreen import printscreen as ps
import base64
import requests
import json





# def imageResolution():
# 解析地址
# url="http://127.0.0.1/ocr"
# #获取截图名称

# print(path)
# r_file = open(path, "rb")
# content = pickle.dumps(r_file.read())
# s = json.dumps({'content': content, 'billModel': '通用OCR'})
# r = requests.post(url, data=s)
# imageResolution()

def read_img_base64(p):
    with open(p, 'rb') as f:
        imgString = base64.b64encode(f.read())
    imgString = b'data:image/jpeg;base64,' + imgString
    return imgString.decode()


def post(billModel='通用OCR'):
    path = ps.window_capture("d:\\")
    URL = 'http://127.0.0.1:8080/ocr'  ##url地址
    imgString = read_img_base64(path)
    headers = {}
    param = {'billModel': billModel,  ##目前支持三种 通用OCR/ 火车票/ 身份证/
             'imgString': imgString, }
    param = json.dumps(param)
    if 1:
        req = requests.post(URL, data=param, headers=None, timeout=5)
        data = req.content.decode('utf-8')
        data = json.loads(data)
    else:
        data = []
    return data


post()
