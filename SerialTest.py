import serial, time
import csv
import numpy as np
from collections import deque
from scipy.signal import savgol_filter

arduino_port = serial.Serial("/dev/cu.usbmodem1411", baudrate=250000)
arduino_port.flush()
arduino_port.reset_input_buffer()

time_step = deque(maxlen=2)

start_time=time.time()


while True:
    while (arduino_port.inWaiting() == 0):
        pass
    try:
        data = arduino_port.readline().decode('utf-8').strip()
        voltage = float(data) / 1024 * 5
        if 0 < voltage < 5:
            # distance = -15.33 * voltage + 43.86
            # print(data)
            # arduino_port.reset_input_buffer()

            run_time = time.time() - start_time
            print([run_time, voltage])
            with open('data.csv', 'at', newline='') as f:
                f_csv = csv.writer(f)
                f_csv.writerow([run_time, voltage])

    except (KeyboardInterrupt, SystemExit, IndexError, ValueError):
        pass


#     if arduino_port.inWaiting() > 0:
#         data = str(arduino_port.readline().decode('utf-8')).strip()
#         if len(data) != 0:
#             voltage = float(data) / 1024 * 5
#             # print(voltage)
#             if 2.3 < voltage < 2.8:
#
#                 distance = -15.33 * voltage + 43.86
#                 print(distance)
#
#                 with open('time stamp.txt', 'at') as f:
#                     # f_csv = csv.writer(f)
#                     # f_csv.writerow(time.clock())
#
#                     print(time.clock(), file=f, end='\n')
#                     print(distance, file=f, end='\n')
#
# except KeyboardInterrupt:
#         print('interrupted!')

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
