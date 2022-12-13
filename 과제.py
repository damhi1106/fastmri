#grobal thresholding
#고급의료영상처리및실습 과제
from tkinter import Image
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("C:/Users/damhI/Downloads/image_00001.png", cv.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

pixel_list = [] #리스트에 픽셀 값 넣기
for i in range(0, 612):
    for j in range(0, 660):
        pixel_list.append(image[i, j])
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

T = [] #T 값을 넣을 빈 리스트 생성
for i in range(110, 130):
    result1_i = filter(up_i, pixel_list)
    result2_i = filter(down_i, pixel_list)
    T_i = (np.mean(list(result1_i)) + np.mean(list(result2_i)))/2
    T.append(T_i)

T_1 = 125 #적절한 초깃값 설정
t = [] #T2 - T1을 넣을 빈 리스트 생성
for i in range(0, 18):
    if T[i+1] - T[i] > 0.5:
        t.append(T[i] - T[i-1])
print("initial T1 : ", T_1) #초기 T1 값
print("final T1 : ", T[len(t)]) #최종 T1 값

ret, final_T1 = cv.threshold(image, T[len(t)], 255, cv.THRESH_BINARY) #최종 T1 값을 기준으로 영상을 분할
ret, initial_T1 = cv.threshold(image, T_1, 255, cv.THRESH_BINARY) #초기 T1 값을 기준으로 영상을 분할

plt.hist(image) #영상의 히스토그램 - 적절한 초깃값 설정
plt.xlabel("pixel value")
plt.ylabel("pixel count")
plt.show()
cv.imshow("original image", image) #original image
cv.imshow("initial T1 image", initial_T1) #초기 T1 값을 기준으로 영상을 분할한 이미지
cv.imshow("final T1 image", final_T1) #최종 T1 값을 기준으로 영상을 분할한 이미지
cv.waitKey(0)
cv.destroyAllWindows()