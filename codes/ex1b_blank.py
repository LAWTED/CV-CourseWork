import cv2


cap = cv2.VideoCapture('../inputs/ebu7240_hand.mp4')

img_array = []

if (cap.isOpened() == False):
    print("Error opening video stream or file")

im_myname = cv2.imread('../inputs/my_name.png')

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#



 





##########################################################################################


out = cv2.VideoWriter('../results/ex1_b_hand_composition.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
