import serial
import time
import pynmea2
import RPi.GPIO as GPIO
from bmp180 import *
import sys

port = '/dev/ttyS0'
baud = 9600
serialPort = serial.Serial(port, baudrate = baud, timeout = 0.5)

print("Timestamp, Latitude, Longitude, Altitude(m), Satellites, Temperature(C),>
sys.stdout.flush() #used to make sure data is written imediatly
while True:
    str = ''
    try:
        str = serialPort.readline().decode().strip()
    except Exception as e:
        print(e)

    if str.find('GGA') > 0:
        msg = None
        try:
            msg = pynmea2.parse(str)
            temperature, pressure = readBmp180()
            print(f"{msg.timestamp}, {round(msg.latitude,6)}, {round(msg.longit>
            sys.stdout.flush()

        except Exception as e:
            print(e)
    time.sleep(0.01)


