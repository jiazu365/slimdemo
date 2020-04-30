# -*- coding:utf-8 -*-
# author: huizhang  time: 2020/4/15

import os
import xml.etree.ElementTree as ET
import shutil

ann_filepath = './Annotations/'
img_filepath = './JPEGImages/'
img_savepath = './newJPEGImages/'
ann_savepath = './newAnnotations/'
if not os.path.exists(img_savepath):
    os.mkdir(img_savepath)

if not os.path.exists(ann_savepath):
    os.mkdir(ann_savepath)

classes = ['bicycle', 'bus', 'car']


def save_annotation(file):

    tree = ET.parse(ann_filepath + '/' + file)
    root = tree.getroot()
    result = root.findall("object")
    bool_num = 0
    for obj in result:
        if obj.find("name").text not in classes:
            root.remove(obj)
        else:
            bool_num = 1
    if bool_num:
        tree.write(ann_savepath + file)
        return True
    else:
        return False


def save_images(file):
    name_img = img_filepath + os.path.splitext(file)[0] + ".jpg"
    shutil.copy(name_img, img_savepath)
    return True


if __name__ == '__main__':
    for f in os.listdir(ann_filepath):
        if save_annotation(f):
           save_images(f)