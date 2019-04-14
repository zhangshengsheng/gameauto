# -*- coding: utf-8 -*-
"""
##图片颜色转换
@author: zs
"""
from PIL import Image

def imgcc(img):
    #print(img.size)  # 打印图片大小
    #print(img.getpixel((4, 4)))
    width = img.size[0]  # 长度
    height = img.size[1]  # 宽度
    for i in range(0, width):  # 遍历所有长度的点
        for j in range(0, height):  # 遍历所有宽度的点
            data = (img.getpixel((i, j)))  # 打印该图片的所有点
            #print(data)  # 打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            #rint(data[0])  # 打印RGBA的r值
            if (data[0] >= 120 and data[1] <= 50 and data[2] <= 50 and  abs(data[1] - data[2])<=12 ):  # RGBA的r值大于170，并且g值大于170,并且b值大于170
                img.putpixel((i, j), (225, 225, 225, 255))  # 则这些像素点的颜色改成大红色
    #img = img.convert("RGB")  # 把图片强制转成RGB
    img.save("D:\\screen\\2019413245145-1.png")
    return img

imgcc(Image.open("D:\\screen\\2.png"))