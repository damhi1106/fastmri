import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import sys

img = cv.imread("C:/Users/damhI/Downloads/image_00001.png", cv.IMREAD_GRAYSCALE)
h,w = img.shape

pixel_list = [] #리스트에 픽셀 값 넣기
for i in range(0, h):
    for j in range(0, w):
        pixel_list.append(img[i, j])
pixel_list.sort()

for i in range(0, 255): #G1, G2를 나누는 기준
    def up_i(num):
        if num > i:
            return num
        else:
            return
    def down_i(num):
        if num <= i:
            return num
        else:
            return




ret, final_T1 = cv.threshold(img, T[len(t)], 255, cv.THRESH_BINARY) #최종 T1 값을 기준으로 영상을 분할
ret, initial_T1 = cv.threshold(img, T1, 255, cv.THRESH_BINARY) #초기 T1 값을 기준으로 영상을 분할


plt.hist(img)
plt.show()
cv.imshow("original image", img) #original image
cv.imshow("initial T1 image", initial_T1) #초기 T1 값을 기준으로 영상을 분할한 이미지
cv.imshow("final T1 image", final_T1) #최종 T1 값을 기준으로 영상을 분할한 이미지
cv.waitKey(0)
cv.destroyAllWindows()