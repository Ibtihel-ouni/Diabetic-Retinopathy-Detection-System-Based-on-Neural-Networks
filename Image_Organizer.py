import numpy as np
import pandas as pd
import os
from shutil import copyfile

df_train = pd.read_csv('try/train.csv')

x_train = df_train['id_code']
y_train = df_train['diagnosis']
os.mkdir("images ")
os.mkdir("images/train")

for i in range(5):
    os.mkdir("images/train/" + str(i))


def make_img_folder(x, y):
    for img_name, diagnosis in zip(x, y):
        if diagnosis == 0:
            copyfile('try/images/train/{}.png'.format(img_name),
                     'images/train/0/{}.jpg'.format(img_name))
        if diagnosis == 1:
            copyfile('try/images/train/{}.png'.format(img_name),
                     'images/train/1/{}.png'.format(img_name))
        if diagnosis == 2:
            copyfile('try/images/train/{}.png'.format(img_name),
                     'images/train/2/{}.png'.format(img_name))
        if diagnosis == 3:
            copyfile('try/images/train/{}.png'.format(img_name),
                     'images/train/3/{}.png'.format(img_name))
        if diagnosis == 4:
            copyfile('try/images/train/{}.png'.format(img_name),
                     'images/train/4/{}.png'.format(img_name))

make_img_folder(x_train, y_train)