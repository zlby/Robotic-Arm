from arduino_control.audio import *
from arduino_control.face import *
from arduino_control.rotate import *
from arduino_control.yolov3.yolo import YOLO
import cv2

if __name__ == '__main__':
    yolo = YOLO()
    while(True):
        print("Please select mode:\n1.Face detection mode.\n2.Audio detection mode.")
        selection = input("Your Choice: ")
        # face detection
        if selection == '1':
            while True:
                pic = get_cam()
                name = myFace_recognition(pic)
                if name != 'Unknown':
                    res = matching(name)
                    break
                print('detection failed, please try again')
            print('detecting ' + name + '.\nFetching ' + res + ' for you....')
            fetch_drug(res, yolo)

        # audio detection
        elif selection == '2':
            r = recoder()
            str = input('please tap r to st1art record ： ')
            count = 0
            while True:
                if str == 'r':
                    r.recoder()
                    r.savewav("test.wav")
                    message = r.wit_identify()
                    print(message)
                    res = r.sort(message)
                    if res:
                        print('succeed.\nFetching ' + res + ' for you...')
                        break
                    else:
                        count += 1
                        str = input('please tap r to start record ： ')
            fetch_drug(res, yolo)
        elif selection == 'quit':
            yolo.close_session()
            pass
        else:
            print("Please enter 1 or 2.")