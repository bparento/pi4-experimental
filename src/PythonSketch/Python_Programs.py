#!/usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print('serial OK')


