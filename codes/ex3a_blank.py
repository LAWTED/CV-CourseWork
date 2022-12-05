# Image stitching using affine transform
import numpy as np
import cv2
import sys
import math
from matplotlib import pyplot as plt

im1 = cv2.imread('../inputs/Img01.jpg')
im2 = cv2.imread('../inputs/Img02.jpg')


im_gray1 = cv2.imread('../inputs/Img01.jpg', 0)
im_gray2 = cv2.imread('../inputs/Img02.jpg', 0)

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#








##########################################################################################

cv2.imwrite('../results/ex3a_stitched_noRANSAC.jpg', panorama_noRANSAC)
cv2.imwrite('../results/ex3a_stitched_RANSAC.jpg', panorama_RANSAC)