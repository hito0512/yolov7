'''
# -*- encoding: utf-8 -*-
# 文件    : loadimg_from_txt.py
# 说明    : 从test.txt文件获取测试图片
# 时间    : 2022/08/11 13:47:22
# 作者    : Hito
# 版本    : 1.0
# 环境    : TensorFlow2.3 or pytorch1.7
'''

import os
import shutil
import random


def color_print(msg):
    no_color = "\033[0m"
    all_color = ['\033[0;%sm'%(str(i)) for i in range(30,38)]
    random_color = random.choice(all_color)
    print('%s%s%s'%(random_color, str(msg), no_color))

def get_img_list(filename):
    img_list=[]
    with open(filename,"rt") as f:
        file = f.readlines()
        file = [f.strip() for f in file]
    return file


def create_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    

def copy_img(path):
    new_path = 'images'
    create_folder(new_path)
    for p in path:
        shutil.copy(p, new_path)


if __name__ == "__main__":
    file_list = get_img_list('../../dataset/test.txt')
    copy_img(file_list)
    
    color_print('done!')