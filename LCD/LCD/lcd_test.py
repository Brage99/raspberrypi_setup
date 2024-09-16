import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time 
from bmp180 import *


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 20
ECHO = 21

# Initialize the LCD with appropriate pin numbers
lcd = CharLCD(numbering_mode=GPIO.BCM,
              cols=16, rows=2,
              pin_rs=24, pin_e=25, pins_data=[23, 22, 27, 17])

# Setup ultrasonic sensor pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Flag to check if GPIO has been setup
gpio_initialized = False

def setup_gpio():
    global gpio_initialized
    if not gpio_initialized:
        gpio_initialized = True

def cleanup_gpio():
    if gpio_initialized:
        GPIO.cleanup()
        lcd.close(clear=True)

def measure_distance():
        

    
    # Ensure the trigger pin is low
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    # Wait for the echo start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    # Wait for the echo end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start
    
    # Calculate distance (pulse_duration * speed of sound / 2)
    distance = pulse_duration * 17150  # 34300/2
    
    # Round to one decimal place
    distance = round(distance, 1)
    
    return distance


def main():
        while True:
                distance = measure_distance()
                temperature, pressure = readBmp180()
                
                # Clear the screen
                lcd.clear()
            
                # Display distance on the LCD
                lcd.write_string(f"Dist: {distance} cm")
                            
                # Wait for 1 second before the next measurement
                time.sleep(1)
                
                # Clear the screen
                lcd.clear()
                
                lcd.write_string(f"Temp: {temperature} C")  
                
                # Wait for 1 second before the next measurement
                time.sleep(1)
                
                # Clear the screen
                lcd.clear()
                
                lcd.write_string(f"Pres: {pressure} Pa")  
                
                # Wait for 1 second before the next measurement
                time.sleep(1)
        cleanup_gpio()
main()
