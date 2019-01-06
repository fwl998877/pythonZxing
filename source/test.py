
import os
from zxing import *
from PIL import Image, ImageEnhance
import file
import shutil
import datetime
import time


def getCode():
    zx = BarCodeReader()
    path = "G:/python-zxing/source/"  # 待读取的文件夹
    path_list = os.listdir(path)
    path_list.sort()  # 对读取的路径进行排序
    arr = []
    arrPath = ""
    flag = 0
    for filename in path_list:
        if filename.endswith('jpg'):
            start = time.process_time()
            arr.append(filename)
            img = Image.open(filename)
            out = img.resize((800, 1000)).convert('L')
            # out = img.convert('L')
            en = ImageEnhance.Contrast(out)
            en_end = en.enhance(2)
            result = en_end.crop((100, 400, 600, 800))
            result.save('tmp.png', 'png')
            barcode = zx.decode('tmp.png')
            code = str(barcode).split("'")[1][0:12]
            end = time.process_time()
            runtime = end-start
            print('图片分析时间  %s 毫秒' % (int(round(runtime * 1000))))

            # print(code)
            path2 = "G:/python-zxing/source/pic/"  # 待读取的文件夹
            # print(arr)
            if(code != ""):
                flag = 1
                file.mkdir(path2+code)
                arrPath = path2+code
        # print(flag)
            if(flag == 1):
                # print("-------------------------------------")
                # for item in arr:
                    # print(item)
                try:
                    shutil.copy(filename, arrPath)
                except IOError:
                    print('cannot COPY')
            if(len(arr) == 3):
                arr = []
                flag = 0
    return


if __name__ == "__main__":
    start = time.perf_counter()
    getCode()
    end = time.perf_counter()
    runtime = end-start
    print('打包所用  %s 毫秒' % (int(round(runtime * 1000))))
