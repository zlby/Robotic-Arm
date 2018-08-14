from arduino_control.yolov3.yolo_video import make_detection
from arduino_control.yolov3.yolo import YOLO, detect_video
from PIL import Image
from pyzbar import pyzbar
from arduino_control.img_hist import *
import time

def get_position_of_box(yolo, message):

    # using yolov3 to detect cups
    boxes = make_detection(yolo, 'images/object.jpg')

    for box in boxes:
        if box['class'] != 'cup':
            continue
        im = Image.open('images/object.jpg')
        region = im.crop((box['left'], box['top'], box['right'], box['bottom']))
        # region.save('box.jpg')
        region_cv = cv2.cvtColor(np.asarray(region), cv2.COLOR_RGB2BGR)
        region_cv = hist_cal(region_cv)
        region = Image.fromarray(cv2.cvtColor(region_cv, cv2.COLOR_BGR2RGB))
        region.save(str(time.ctime()).replace(':', ' ') + 'box.jpg')
        detect_objs = pyzbar.decode(region)

        # if there is no box detected, return -1
        if len(detect_objs) == 0:
            continue

        # detect qr code information
        qrdata = str(detect_objs[0].data, encoding='utf-8')

        # if the qrcode is not what we want, go ahead to another one
        if qrdata != message:
            continue

        middle_point  = int(round((box['left'] + box['right']) / 2))

        return middle_point

    return -1

if __name__ == '__main__':
    print(get_position_of_box('drug A'))