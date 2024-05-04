#!/usr/bin/env python
# coding: utf-8

from matplotlib import pyplot as plt
from skimage import io, transform, color
import os


size = (75, 150)
density = '        _.,-=+:;cba!?0123456789$W#@Ñ'


def img_init(img):
    img = transform.resize(img, size)
    img = (img * 255).astype('uint8')
    return img


def makeText(img):
    ascii_img = ''
    for i in range(size[0]):
        for j in range(size[1]):
            ascii_img += density[int(((img[i, j]) / 255) * len(density))]
        ascii_img += '\n'
    return ascii_img


if __name__ == '__main__':
    img1 = io.imread('cat.jpg', as_gray=True)
    img = img_init(img1)
    os.system('cls')
    print(makeText(img))

    fig, axs = plt.subplots(1, 2)
    fig.suptitle('images')
    axs[0].imshow(img1, cmap='gray')
    axs[1].imshow(img, cmap='gray')
    plt.show()