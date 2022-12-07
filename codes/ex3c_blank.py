# Window-based stereo matching
import numpy as np
import cv2


def matching_cost_computation(matching_cost, left_img, right_img, d_max):
    # Matching cost computation: SSD
    h, w = left_img.shape

    for y in range(h):
        for x in range(w):
            for d in range(d_max):
                if x - d >= 0:
                    temp_cost = float(left_img[y, x]) - float(right_img[y, x - d])
                    matching_cost[y, x, d] = temp_cost * temp_cost


def cost_aggregation_window(aggregated_cost, matching_cost, kernel, d_max):
    # --------------------------------- WRITE YOUR CODE HERE ---------------------------------#
    # NO OPENCV FUNCTION IS ALLOWED HERE
    h, w = left_img.shape
    for y in range(h):
        for x in range(w):
            for d in range(d_max):
                for k in range(-kernel//2, kernel//2+1):
                    dy, dx = y + k, x + k
                    if dy >= 0 and dy < h and dx >= 0 and dx < w:
                        aggregated_cost[y, x, d] += matching_cost[dy, dx, d]









    ##########################################################################################


def disparity_estimation(disparity, aggregated_cost, d_max):
    offset_adjust = 255 / d_max  # this is used to map disparity map output to 0-255 range
    h, w = disparity.shape
    for y in range(h):
        for x in range(w):
            best_offset = 0
            prev_ssd = 65534
            for d in range(d_max):
                if aggregated_cost[y, x, d] < prev_ssd:
                    prev_ssd = aggregated_cost[y, x, d]
                    best_offset = d

            # set disparity output for this x,y location to the best match
            disparity[y, x] = best_offset * offset_adjust


if __name__ == '__main__':
    # Load left and right images and convert to grayscale for simplicity
    left_img = cv2.imread('../inputs/teddy_im2.png', 0)
    right_img = cv2.imread('../inputs/teddy_im6.png', 0)

    h, w = left_img.shape
    d_max, kernel_size = 32, 3

    matching_cost = np.zeros((h, w, d_max), np.float64)
    aggregated_cost = np.zeros((h, w, d_max), np.float64)
    disparity = np.zeros((h, w), np.uint8)

    matching_cost_computation(matching_cost, left_img, right_img, d_max)
    ## COMPLETE THIS FUNCTION
    cost_aggregation_window(aggregated_cost, matching_cost, kernel_size, d_max)
    ##
    disparity_estimation(disparity, aggregated_cost, d_max)
    cv2.imwrite('../results/ex3c_w_3.png', disparity)
    print('done1')

    d_max, kernel_size = 32, 11

    matching_cost = np.zeros((h, w, d_max), np.float64)
    aggregated_cost = np.zeros((h, w, d_max), np.float64)
    disparity = np.zeros((h, w), np.uint8)

    matching_cost_computation(matching_cost, left_img, right_img, d_max)
    ## COMPLETE THIS FUNCTION
    cost_aggregation_window(aggregated_cost, matching_cost, kernel_size, d_max)
    ##
    disparity_estimation(disparity, aggregated_cost, d_max)
    cv2.imwrite('../results/ex3c_w_11.png', disparity)
    print('done2')
