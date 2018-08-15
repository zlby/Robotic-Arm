import sys
import time
import serial
# from arduino_control.cam_control import *
from arduino_control.catch_image import get_position_of_box
from arduino_control.yolov3.yolo import YOLO
import numpy as np
import cv2


port = 'COM3'
ard = serial.Serial(port,9600,timeout=5)
global initial_speed, rotate_degree, rotate_times
initial_speed = -4
rotate_degree = 1
rotate_times = 0
screen_mid = 320

def object_detecting(x_pos, current_pos):
    """检测物体，未检测到前循环旋转"""
    global initial_speed
    if x_pos < 0:
        if x_pos == -1:
            current_pos = current_pos + initial_speed
        else:
            current_pos = current_pos + initial_speed/2
        if current_pos < 5:
            initial_speed = -initial_speed
        elif current_pos > 96:
            initial_speed = -initial_speed
        else:
            info = str(6) + ',' + str(current_pos)
            #print(current_pos)
            ard.write(str.encode(info))
            if x_pos == -2:
                time.sleep(0.3)
        return True, current_pos

    else:
        return False, current_pos



def centroid_detecting(x_pos, current_pos):
    global rotate_times, rotate_degree
    global screen_mid #屏幕中心点

    if x_pos < 0:
        seed = np.random.randint(2)
        if seed == 0:
            current_pos += 1
        else:
            current_pos -= 1
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
        return False, current_pos

    if abs(x_pos - screen_mid) < 10:
        return True, current_pos

    elif x_pos > screen_mid:
        current_pos = current_pos - rotate_degree
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
    else:
        current_pos = current_pos + rotate_degree
        info = str(6) + ',' + str(current_pos)
        ard.write(str.encode(info))
    return False, current_pos


def write_port(device, value, current_pos):
    info = str(device) + ',' + str(current_pos)

    if current_pos < value:
        for i in range(value - current_pos):
            current_pos += 1
            info = str(device) + ',' + str(current_pos)
            ard.write(str.encode(info))
            time.sleep(1)

    else:
        for i in range(current_pos - value):
            current_pos -= 1
            info = str(device) + ',' + str(current_pos)
            ard.write(str.encode(info))
            time.sleep(1)

    time.sleep(1)  # delay


def grab():
    info = '0,0'
    ard.write(str.encode(info))
    # ELBOW = 1
    # SHOULDER = 2
    # WRISTz = 5
    # claw = 7
    #
    # # round 1
    # write_port(ELBOW, 76, 110)
    #
    # write_port(SHOULDER, 76, 68)
    #
    # write_port(WRISTz, 96, 65)
    #
    # write_port(claw, 0, 30)
    #
    # time.sleep(0.5)

    # round 2
    # write_port(ELBOW, 56, 76)
    # write_port(SHOULDER, 85, 76)
    # write_port(WRISTz, 105, 96)
    # time.sleep(0.5)

    # round 3
    # write_port(ELBOW, 34, 56)
    # write_port(SHOULDER, 73, 85)
    # time.sleep(0.5)

    # round 4
    # write_port(ELBOW, 21, 34)
    # write_port(SHOULDER, 63, 73)
    # time.sleep(0.5)

    # round 5

    # write_port(ELBOW, 60, 21)
    # write_port(SHOULDER, 63, 63)
    # write_port(claw, 30)

    # time.sleep(0.5)
def grab_drug(message):
    print(message)

def fetch_drug(message, yolo):
    base_list = []

    current_position = 96
    cap = cv2.VideoCapture(1)
    count = 0
    while(True):
        count += 1
        time.sleep(0.2)
        ret, frame = cap.read()
        time.sleep(0.1)
        # print(count)
        cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        name = 'images/object.jpg'
        cv2.imwrite(name, frame)
            # break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        position = get_position_of_box(yolo, message)

        flag, current_position = object_detecting(position, current_position)

        if not flag:
            stop = False
            init_direction = np.sign(position - screen_mid)
            while(not stop):
                time.sleep(0.3)
                ret, frame = cap.read()
                # print(count)
                cv2.imshow('frame', frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                name = 'images/object.jpg'
                cv2.imwrite(name, frame)
                stop, current_position = centroid_detecting(position, current_position)
                position = get_position_of_box(yolo, message, False)

                direction = np.sign(position - screen_mid)
                if direction != init_direction:
                    stop = True

                base_list.append(current_position)
            break

    grab()
    # yolo.close_session()
    cap.release()
    cv2.destroyAllWindows()


