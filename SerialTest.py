import serial, time
from collections import deque

arduino_port = serial.Serial("/dev/cu.usbmodem1411", baudrate=9600)
time_step = deque(maxlen=2)

while True:
    if arduino_port.inWaiting() > 0:
        data = str(arduino_port.readline().decode('utf-8')).strip()
        if len(data) != 0:
            print(float(data))
            with open('time stamp.txt', 'at') as f:
                voltage = float(data) / 1024 * 2.5
                print(voltage, file=f, end='\n')

        # time_step.append(time.clock())
        # if len(time_step) != 1:
        #     temp_copy = list(time_step)
        #     with open('time stamp.txt', 'at') as f:
        #         voltage = int(data) / 1024 * 2.5
        #         print(voltage, file=f, end='\n')

# hi i'm ru
# while True:
#     if arduino_port.inWaiting() > 0:
#         try:
#             data = str(arduino_port.readline().decode('utf-8')).strip()
#             print(data)
#         except KeyboardInterrupt:
#             print("Quit!")
