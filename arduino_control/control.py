import serial
import time

#The following line is for serial over GPIO
port = 'COM3'


ard = serial.Serial(port,9600,timeout=5)


while(True):
    deviceNo = input("Please choose device: ")
    angle = input("Please enter the angle to rotate: ")

    if deviceNo == 'exit' or angle == 'exit':
        break

    info = str(deviceNo) + ',' + str(angle)

    ard.write(str.encode(info))

    time.sleep(1)