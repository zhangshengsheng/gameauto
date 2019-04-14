# -*- coding: utf-8 -*-
"""
##坐标转换函数
@author: zs
"""

import random
import win32api, win32gui, win32con
from ctypes import *
import time
from kit.vkcode import VK_CODE


def getcoordina(box):
    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]
    x3 = box[4]
    y3 = box[5]
    x4 = box[6]
    y4 = box[7]
    while True:
        x = random.gauss((x1 + x2) / 2, abs(x1 - x2))
        if x1 < x < x2:
            break
    print(x)
    while True:
        y = random.gauss((y1 + y3) / 2, abs(y1 - y3))
        if y1 < y < y3:
            break
    return x,y

def resize_im(imgRate, scale, max_scale):
    f = scale / min(imgRate)
    if f * max(imgRate) > max_scale:
        f = max_scale / max(imgRate)
    newW = imgRate[0] * f
    newH = imgRate[1] * f
    return newW, newH, f

def mouse_move(x, y):
    windll.user32.SetCursorPos(int(x), int(y))


def mouse_click(x=None, y=None):
    if not x is None and not y is None:
        mouse_move(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_dclick(x=None, y=None):
    if not x is None and not y is None:
        mouse_move(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def key_input(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c], 0, 0, 0)
        win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.01)
# 坐标获取处理
# getcoordina()
