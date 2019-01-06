
import os
from zxing import *
import tkinter.filedialog as filedialog
from tkinter import *
from tkinter import *
from PIL import Image, ImageEnhance
import file
import shutil
import datetime
import time
import io

def getCode(readPath, locationPath):
    zx = BarCodeReader()
    # path = "G:/python-zxing/source/"  # 待读取的文件夹
    path_list = os.listdir(readPath)
    path_list.sort()  # 对读取的路径进行排序
    arr = []
    arrPath = ""
    flag = 0
    for filename in path_list:
        if filename.endswith('jpg'):
            start = time.process_time()
            arr.append(filename)
            img = Image.open(os.path.join(readPath, filename))
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
            # path2 = "G:/python-zxing/source/pic/"  # 待读取的文件夹
            # print(arr)
            if(code != ""):
                flag = 1
                file.mkdir(os.path.join(locationPath, code))
                arrPath =os.path.join(locationPath, code)
        # print(flag)
            if(flag == 1):
                # print("-------------------------------------")
                # for item in arr:
                    # print(item)
                try:
                    shutil.copy(os.path.join(readPath, filename), arrPath)
                except IOError:
                    print('cannot COPY')
            if(len(arr) == 3):
                arr = []
                flag = 0
    return


if __name__ == "__main__":
    global readPath
    global locationPath
    readPath = filedialog.askdirectory()
    locationPath = filedialog.askdirectory()
    print(readPath)
    print(locationPath)
    start = time.perf_counter()
    getCode(readPath, locationPath)
    end = time.perf_counter()
    runtime = end-start
    print('打包所用  %s 毫秒' % (int(round(runtime * 1000))))
