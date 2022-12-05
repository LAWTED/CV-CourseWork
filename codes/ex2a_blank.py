# Gaussian filtering without OpenCV
import numpy as np
import cv2

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#
# You can define functions here
# NO OPENCV FUNCTION IS ALLOWED HERE














##########################################################################################


im_gray = cv2.imread('../inputs/lena.jpg', 0)
im_gray = cv2.resize(im_gray, (256, 256))

result_gf1 = gaussian_filter_gray(im_gray, 5, 1.0)
result_gf2 = gaussian_filter_gray(im_gray, 5, 10.0)
result_gf3 = gaussian_filter_gray(im_gray, 11, 1.0)
result_gf4 = gaussian_filter_gray(im_gray, 11, 10.0)

result_gf1 = np.uint8(result_gf1)
result_gf2 = np.uint8(result_gf2)
result_gf3 = np.uint8(result_gf3)
result_gf4 = np.uint8(result_gf4)

cv2.imwrite('../results/ex2a_gf_5_1.jpg', result_gf1)
cv2.imwrite('../results/ex2a_gf_5_10.jpg', result_gf2)
cv2.imwrite('../results/ex2a_gf_11_1.jpg', result_gf3)
cv2.imwrite('../results/ex2a_gf_11_10.jpg', result_gf4)
