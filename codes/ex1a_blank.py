import cv2
import numpy as np


cap = cv2.VideoCapture('../inputs/ebu7240_hand.mp4')

img_array = []

if (cap.isOpened() == False):
    print("Error opening video stream or file")

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#

# resize the video
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (640, 360)


# count = 1
# success, frame_src = cap.read()
# video_write = cv2.VideoWriter('../outputs/ebu7240_hand.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)

# while success and count <= 90:
#     frame_target = cv2.resize(frame_src, size)
#     video_write.write(frame_target)
#     success, frame_src = cap.read()
#     count += 1
# cv2.destroyWindow("video")
# cap.release()

count = 1
success, frame = cap.read()
height, width, layers = frame.shape
zeroImgMatrix = np.zeros((height, width), dtype="uint8")
while success:
    b, g, r = cv2.split(frame)
    if 1 <= count <= 30:
        img_array.append(frame)
    if 31 <= count <= 50:
        # Zero values to R, G channel
        B = cv2.merge([b, zeroImgMatrix, zeroImgMatrix])
        img_array.append(B)
    elif 51 <= count <= 70:
        # Zero values to B, G channel
        R = cv2.merge([zeroImgMatrix, zeroImgMatrix, r])
        img_array.append(R)
    elif 71 <= count <= 90:
        # Zero values to R, B channel
        G = cv2.merge([zeroImgMatrix, g, zeroImgMatrix])
        img_array.append(G)


    # save the frame
    if count in [1, 21, 31, 61 ,90]:
        cv2.imwrite('../results/ex1-frame%d.jpg' % count, img_array[count-1])
    success, frame = cap.read()
    count += 1

##########################################################################################

out = cv2.VideoWriter('../results/ex1_a_hand_rgbtest.mp4',
                      cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
for img in img_array:
    out.write(img)
out.release()

