# Bilateral filtering without OpenCV
import numpy as np
import cv2
import sys
import math


#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#
# You can define functions here
# NO OPENCV FUNCTION IS ALLOWED HERE











##########################################################################################


im_gray = cv2.imread('../inputs/cat.png',0)

result_bf1 = bilateral_filter_gray(im_gray, 11, 30.0, 3.0)
result_bf2 = bilateral_filter_gray(im_gray, 11, 30.0, 30.0)
result_bf3 = bilateral_filter_gray(im_gray, 11, 100.0, 3.0)
result_bf4 = bilateral_filter_gray(im_gray, 11, 100.0, 30.0)
result_bf5 = bilateral_filter_gray(im_gray, 5, 100.0, 30.0)

result_bf1 = np.uint8(result_bf1)
result_bf2 = np.uint8(result_bf2)
result_bf3 = np.uint8(result_bf3)
result_bf4 = np.uint8(result_bf4)
result_bf5 = np.uint8(result_bf5)


cv2.imwrite('../results/ex2b_bf_11_30_3.jpg', result_bf1)
cv2.imwrite('../results/ex2b_bf_11_30_30.jpg', result_bf2)
cv2.imwrite('../results/ex2b_bf_11_100_3.jpg', result_bf3)
cv2.imwrite('../results/ex2b_bf_11_100_30.jpg', result_bf4)
cv2.imwrite('../results/ex2b_bf_5_100_30.jpg', result_bf5)

