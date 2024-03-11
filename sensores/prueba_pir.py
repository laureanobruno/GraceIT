import time
import RPi.GPIO as GPIO

pir = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)

while True:
    print(GPIO.input(pir))