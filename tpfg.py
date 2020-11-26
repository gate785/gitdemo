#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/10 19:43
# @Author : Zyf
# @File : tpfg.py
# @Software: PyCharm
import os
import time

import cv2
import numpy as np

# ----------------------------------------------------------------------------------------------------------------
# --脚本所支持的文件扩展名
supExpName = ["jpg", "png"]

countNum = 0  # --处理图片计数

print("该脚本将脚本所在目录的所支持的图片拆分为宽度为原来1/2的两个图片")
print("--程序将在5s后自动执行--脚本执行需要使用 cv2库--")
print("--使用 pip install opencv-python 命令可以安装该库--")
print("Loading", end="")
for i in range(10):
    print(".", end='', flush=True)
    time.sleep(0.5)
# ----------------------------------------------------------------------------------------------------------------
# --获取当前路径
in_dir = os.path.abspath('.') + "/"
# --设置输出路径
out_dir = os.path.abspath('.') + "/out_dir/"

# 判断输出文件夹是否存在，若不存在则创建
if not os.path.exists(out_dir):
    os.mkdir("out_dir")
    print("创建输出目录")


# ----------------------------------------------------------------------------------------------------------------
# --打开图片
def cv_imread(in_pash):
    cv_img = cv2.imdecode(np.fromfile(in_pash, dtype=np.uint8), -1)  # -1表示cv2.IMREAD_UNCHANGED
    print(os.path.basename(in_pash) + "\t宽&高", cv_img.shape[1], cv_img.shape[0])
    return cv_img


# --保存图片
def cv_imwrite(out_path, img_mp):
    cv2.imencode('.png', img_mp)[1].tofile(out_path)


# ----------------------------------------------------------------------------------------------------------------
# --遍历 in_dir 路径下所有文件
for file_name in os.listdir(in_dir):
    extName = os.path.splitext(file_name)[-1][1:]  # --分离并截取扩展名
    extName = extName.lower()  # --将取得的扩展名转为小写

    # --判断文件是否为所支持的图片格式
    if extName in supExpName:
        countNum = countNum + 1;
        print("\n正在处理第 %d 张图片" % (countNum))
        img = cv_imread(in_dir + file_name)
        h, w, w2 = img.shape[0], img.shape[1], img.shape[1] // 2
        # print(h,w,w2)

        # print(os.getcwd())  #--这个命令可以用来获取当前脚本所在目录--
        img_name = file_name.split('.')[0]

        cropped1 = img[0:int(h), 0:int(w2)]
        cropped2 = img[0:int(h), int(w2):int(w)]
        cv_imwrite(out_dir + img_name + "-1" + ".png", cropped1)
        cv_imwrite(out_dir + img_name + "-2" + ".png", cropped2)

print("--complete--")