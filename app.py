# -*- coding: utf-8 -*-
"""
##主函数
@author: zs
"""
import  coordinatetranslation
import imageResolution as ir
def main():
    data, imgRate = ir.post()
    # print(str(type(data['res'])))
    for res in data['res']:
        # print(res['text'])
        if (res['text'] == '下一步'):
            box = res['box']
            coordinatetranslation.getcoordina(box)
            # print(res['box'])

    # print(resize_im(imgRate, 1920, 1080))
if __name__ == '__main__':
    main()