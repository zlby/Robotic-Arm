import cv2

xr_robot=0
yr_robot=0
zr_robot=0

xg_robot=0
yg_robot=0
zg_robot=0

xb_robot=0
yb_robot=0
zb_robot=0

cm_por_pixel = 0

# get image from webcam
cap = cv2.VideoCapture(1)
ret, frame = cap.read()

(B,G,R) = cv2.split(frame)

print('finish')