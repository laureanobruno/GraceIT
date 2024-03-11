import RPi.GPIO as GPIO
import time

lamp = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(lamp) == GPIO.LOW:
        print("Lampara encendida")
    else:
        print("Lampara apagada")
    time.sleep(0.5)
