import serial
import time

port = 'COM3'
ard = serial.Serial(port, 9600, timeout=5)

def write_port(device,value,current_pos):
    info = str(device) + ',' + str(current_pos)

    if current_pos < value:
        for i in range(value - current_pos):
            current_pos += 1
            ard.write(str.encode(info))
            time.sleep(0.005)

    else:
        for i in range(current_pos - value):
            current_pos -= 1
            ard.write(str.encode(info))
            time.sleep(0.005)

    time.sleep(0.2)  #delay


def grab():
    ELBOW = 1
    SHOULDER = 2
    WRISTz = 5
    claw = 7

    # round 1
    write_port(ELBOW,76)

    write_port(SHOULDER,76)

    write_port(WRISTz,96)

    write_port(claw,0)

    time.sleep(0.5)

    #round 2
    write_port(ELBOW, 56)
    write_port(SHOULDER, 85)
    write_port(WRISTz, 105)
    time.sleep(0.5)

    #round 3
    write_port(ELBOW, 34)
    write_port(SHOULDER, 73)
    time.sleep(0.5)

    #round 4
    write_port(ELBOW, 21)
    write_port(SHOULDER, 63)
    time.sleep(0.5)

    #round 5

    write_port(ELBOW, 60)
    write_port(SHOULDER, 63)
    write_port(claw,30)
    
    time.sleep(0.5)
