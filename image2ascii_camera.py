#!/usr/bin/env python
# coding: utf-8

import os
import cv2
import numpy as np
from numba import njit

size = (150, 75)
density = '        .,-=+*:;cba!?0123456789$W#@Ñ'
Cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def img_init():
    ret, img = Cam.read()
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    # img = cv2.GaussianBlur(img, (3, 3), 0)
    # img = cv2.threshold(img, 50, 200, cv2.THRESH_BINARY)[1]

    return img


@njit(cache=True)
def makeText(img):
    ascii_img = ''
    for i in range(size[1]):
        for j in range(size[0]):
            x = int(remap(img[i, j], 0, 255, 0, len(density) - 1))
            ascii_img += density[x]
        ascii_img += '\n'
    return ascii_img


@njit(cache=True)
def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


if __name__ == '__main__':
    window_name = 'ASCII Camera'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    while True:
        img = img_init()
        txt = makeText(img)
        os.system('cls')
        print(txt)
        cv2.imshow(window_name, img)

        if cv2.waitKey(2) >= 0:
            break
