import numpy as np
import cv2
import os
import time
import face_recognition

unknown_pic_path = '/Users/wonderful_xue/Desktop/project/unknown_pictures'
known_pic_path = '/Users/wonderful_xue/Desktop/project/known_people'

def get_cam():
    # webcam 的代号是 1 ，电脑自带前置摄像头是 0
    cap = cv2.VideoCapture(1)
    count = 0
    if cap.isOpened():

        tag = time.ctime()
        name = ''
        while (True):

            count = count + 1
            # Capture frame-by-frame
            ret, frame = cap.read()
            print(count)
            cv2.imshow('frame', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            if count % 4 == 0:
                name = 'save' + str(tag) + '.jpg'
                name = os.path.join(unknown_pic_path, name)
                cv2.imwrite(name, frame)
                # break

            elif cv2.waitKey(1) & 0xFF == ord('q') :
                break

            # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        return name
    else:
        raise Exception('reboot the camera')

def myFace_recognition(pic):

    # Load known pictures and learn how to recognize it.
    yang_image = face_recognition.load_image_file(os.path.join(known_pic_path, 'yang.jpg'))
    yang_face_encoding = face_recognition.face_encodings(yang_image)[0]

    yao_image = face_recognition.load_image_file(os.path.join(known_pic_path, 'yao.jpg'))
    yao_face_encoding = face_recognition.face_encodings(yao_image)[0]

    known_face_encodings = [
        yang_face_encoding,
        yao_face_encoding
    ]

    known_face_names = [
        "Yang Yuzheng",
        "yao Ruigang"
    ]

    # Load unknown_face
    unknown_image = face_recognition.load_image_file(pic)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

    print("Is the unknown face a picture of Yang Yuzheng? {}".format(results[0]))
    print("Is the unknown face a picture of Yao Ruigang? {}".format(results[1]))
    print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

if __name__ == '__main__':
    get_cam()



