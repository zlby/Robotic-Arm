from arduino_control.yolov3.yolo_video import make_detection
from arduino_control.yolov3.yolo import YOLO, detect_video
from PIL import Image
from pyzbar.pyzbar import decode

boxes = make_detection(YOLO(), 'qrcode.jpg')

for box in boxes:
    if box['class'] != 'cup':
        continue
    print(box['class'])
    im = Image.open('qrcode.jpg')
    region = im.crop((box['left'], box['top'], box['right'], box['bottom']))
    region.save('box.jpg')
    print(decode(Image.open('box.jpg')))