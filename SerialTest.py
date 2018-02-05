import serial, time
from collections import deque

arduino_port = serial.Serial("/dev/cu.usbmodem1421", baudrate=9600)
time_step = deque(maxlen=2)

# while True:
#     if arduino_port.inWaiting() > 0:
#         data = str(arduino_port.readline().decode('utf-8')).strip()
#         print(data)
#         time_step.append(time.clock())
#         if len(time_step) != 1:
#             temp_copy = list(time_step)
#             with open('time stamp.txt', 'at') as f:
#                 print(temp_copy[1] - temp_copy[0], file=f, end='\n')


# hi i'm ru

while True:
    if arduino_port.inWaiting() > 0:
        try:
            data = str(arduino_port.readline().decode('utf-8')).strip()
            print(data)
        except KeyboardInterrupt:
            print("Quit!")