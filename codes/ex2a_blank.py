# Gaussian filtering without OpenCV
import numpy as np
import cv2

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#
# You can define functions here
# NO OPENCV FUNCTION IS ALLOWED HERE


# Implement gaussian filtering using a grayscale lena.jpg as an input.
# See the results with varying the window size, W=5,11, and the standard deviation, σ_s=1,10 .

def gaussian_kernel(W, sigma):
    k = np.zeros((W, W))
    for i in range(W):
        for j in range(W):
            k[i, j] = np.exp(-((i-W//2)**2 + (j-W//2)**2) / (2*sigma**2))
    k = k / np.sum(k)
    return k

def gaussian_filter_gray(img, W, sigma):
    # W: window size
    # sigma: standard deviation
    # img: input image
    # img_out: output image
    # YOUR CODE HERE
    img_out = np.zeros(img.shape)
    img_pad = np.pad(img, ((W//2, W//2), (W//2, W//2)), 'edge')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_out[i, j] = np.sum(img_pad[i:i+W, j:j+W] * gaussian_kernel(W, sigma))
    return img_out


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
