# -*- coding: utf-8 -*-
"""
##截屏函数
@author: zs
"""

import time
from PIL import Image
import os
import win32gui, win32ui, win32con, win32api
import numpy as np
from PIL import ImageGrab


class printscreen:

    def window_capture(dpath):
        '''''
      截屏函数,调用方法window_capture('d:\\') ,参数为指定保存的目录
      返回图片文件名,文件名格式:日期.jpg 如:2009328224853.jpg
        '''

        hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　#图片大小
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        cc = time.gmtime()
        bmpname = str(cc[0]) + str(cc[1]) + str(cc[2]) + str(cc[3] + 8) + str(cc[4]) + str(cc[5]) + '.bmp'
        saveBitMap.SaveBitmapFile(saveDC, bmpname)
        Image.open(bmpname).save(bmpname[:-4] + ".jpg")
        os.remove(bmpname)
        jpgname = bmpname[:-4] + '.jpg'
        djpgname = dpath + jpgname
        copy_command = "move %s %s" % (jpgname, djpgname)
        os.popen(copy_command)
        return bmpname[:-4] + '.jpg'

    def python_captrue():
        # 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
        beg = time.time()
        debug = False
        for i in range(10):
            img = ImageGrab.grab()
            img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)

        end = time.time()
        print(end - beg)


    # window调用截屏函数
    # window_capture('d:\\')
    # python调用截图函数
    # python_captrue()
