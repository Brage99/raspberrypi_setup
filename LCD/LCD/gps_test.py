import serial
import time

# Open serial port
ser = serial.Serial(
    port='/dev/serial0',      # Use the appropriate serial port for Pi 4
    baudrate=9600,            # Set baudrate, adjust as per your needs
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1                 # Set timeout to 1 second
)

try:
    while True:
        if ser.in_waiting > 0:
            # Read a line of input from the serial port
            = ser.readline().decode('utf-8').rstrip()
            print("Received:", data)
        else:
            # Wait and check again
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    # Close the serial port
    ser.close()
