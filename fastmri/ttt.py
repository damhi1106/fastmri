import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
np.set_printoptions(threshold=sys.maxsize)
from matplotlib import pyplot as plt

img = cv2.imread("C:/Users/damhI/Downloads/image_00001.png", cv2.IMREAD_GRAYSCALE)

T1 = 125
G1 = np.where(img > T1, 0, img)
G2 = np.where(img < T1, 0, img)

T2 = 0.5*(np.mean(G1)+np.mean(G2))
J = abs(T1-T2)
print("뺸거", J)

ret, VT1 = cv2.threshold(img, T1, 255, cv2.THRESH_BINARY) #초기 T1 값을 기준으로 영상을 분할
ret, VT2 = cv2.threshold(img, T2, 255, cv2.THRESH_BINARY) #초기 T1 값을 기준으로 영상을 분할

cv2.imshow('image', img)
# cv2.imshow('1', G1)
# cv2.imshow('2', G2)
cv2.imshow('T1', VT1)
cv2.imshow('T1', VT2)


cv2.waitKey()
plt.hist(img) #영상의 히스토그램 - 적절한 초깃값 설정
plt.xlabel("pixel value")
plt.ylabel("pixel count")
plt.show()

cv2.waitKey()

#print ("________________________", G1)
print ("________________________", G2)

# T2 = 0.5*(np.mean(G1)+np.mean(G2))
# print (T2)
# J = abs(T1-T2)
# print("뺸거", J)