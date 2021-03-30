#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import cv2
import numpy as np


def main():
  imgA = cv2.imread('dog0.jpg')
  imgB = cv2.imread('dog1.jpg')
  #在进行拼接之前，必须将两个img resize成同一个size,
  #因为np.hstack和np.vstack实际上是堆叠数组，不过按照列和行进行堆叠数组
  size = (300, 300)
  imgA = cv2.resize(imgA, size)
  imgB = cv2.resize(imgB, size)
  #水平拼接
  splice0 = np.hstack((imgA, imgB))
  #垂直拼接
  splice1 = np.vstack((imgA, imgB))
  cv2.imshow('splice0', splice0)
  cv2.waitKey()
  cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
