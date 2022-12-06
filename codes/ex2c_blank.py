# Median filtering without OpenCV
import numpy as np
import cv2
import sys
import math
from matplotlib import pyplot as plt


#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#
# You can define functions here
# NO OPENCV FUNCTION IS ALLOWED HERE


# Generate images with gaussian noise (ex2c_gnoise.jpg) and salt noise (ex2c_inoise.jpg) using a greyscale cat.png as an input.

def median_filter_gray(img, kernel):
    H, W = img.shape
    pad = kernel // 2
    out = np.zeros((H + pad * 2, W + pad * 2))
    out[pad:pad + H, pad:pad + W] = img
    tmp = out.copy()
    # filtering
    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = np.median(tmp[y: y + kernel, x: x + kernel])
    out = out[pad: pad + H, pad: pad + W]
    return out









##########################################################################################


im_gray = cv2.imread('../inputs/cat.png',0)
im_gray = cv2.resize(im_gray, (256,256))

gaussian_noise = np.zeros((im_gray.shape[0], im_gray.shape[1]),dtype=np.uint8)#
gaussian_noise = cv2.randn(gaussian_noise, 128, 20)

uniform_noise = np.zeros((im_gray.shape[0], im_gray.shape[1]),dtype=np.uint8)
uniform_noise = cv2.randu(uniform_noise,0,255)
ret, impulse_noise = cv2.threshold(uniform_noise,220,255,cv2.THRESH_BINARY)

gaussian_noise = (gaussian_noise*0.5).astype(np.uint8)
impulse_noise = impulse_noise.astype(np.uint8)

imnoise_gaussian = cv2.add(im_gray, gaussian_noise)
imnoise_impulse = cv2.add(im_gray, impulse_noise)


cv2.imwrite('../results/ex2c_gnoise.jpg', np.uint8(imnoise_gaussian))
cv2.imwrite('../results/ex2c_inoise.jpg', np.uint8(imnoise_impulse))


result_original_mf = median_filter_gray(im_gray, 5)
result_gaussian_mf = median_filter_gray(imnoise_gaussian, 5)
result_impulse_mf = median_filter_gray(imnoise_impulse, 5)

cv2.imwrite('../results/ex2c_original_median_5.jpg', np.uint8(result_original_mf))
cv2.imwrite('../results/ex2c_gnoise_median_5.jpg', np.uint8(imnoise_gaussian))
cv2.imwrite('../results/ex2c_inoise_median_5.jpg', np.uint8(result_impulse_mf))

#
result_original_mf = median_filter_gray(im_gray, 11)
result_gaussian_mf = median_filter_gray(imnoise_gaussian, 11)
result_impulse_mf = median_filter_gray(imnoise_impulse, 11)

cv2.imwrite('../results/ex2c_original_median_11.jpg', np.uint8(result_original_mf))
cv2.imwrite('../results/ex2c_gnoise_median_11.jpg', np.uint8(result_gaussian_mf))
cv2.imwrite('../results/ex2c_inoise_median_11.jpg', np.uint8(result_impulse_mf))

