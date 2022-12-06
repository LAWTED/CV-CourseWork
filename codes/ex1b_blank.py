import cv2


cap = cv2.VideoCapture('../inputs/ebu7240_hand.mp4')

img_array = []

if (cap.isOpened() == False):
    print("Error opening video stream or file")

im_myname = cv2.imread('../inputs/my_name.png')

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#

count = 1
img_height, img_width, img_layers = im_myname.shape
frame_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
y = frame_height - img_height
x = 0
size = (640, 360)
success, frame = cap.read()
while success:
    # The location of the image I starts from the bottom left of the frame (F_1).
    # Then shift the location of the image I, 2 pixels horizontally to the right in every frame.
    # add image to frame
    frame[ y:y+img_height , x:x+img_width ] = im_myname
    img_array.append(frame)
    # Display the resulting frame
    x += 2
    if count in [1, 21, 31, 61 ,90]:
        cv2.imwrite('../results/ex1b/frame%d.jpg' % count, img_array[count-1])
    success, frame = cap.read()
    count += 1





##########################################################################################


out = cv2.VideoWriter('../results/ex1_b_hand_composition.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()