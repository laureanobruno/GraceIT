
from playsound import playsound
import time
from sensores.funciones_sensores import *
import cv2

from threading import Thread


def playy():
    playsound('ImagenesDisenio/graceSilbando.mp3')

pir = 12
trig = 23
echo = 24
lamp = 25
pin_3v = 2
green_led = 16
blue_led = 20
ultima_gente = False
last_chist = -99
def inicio_sensores(GPIO, servo):
    # T = Thread(target=playy) # create thread
    ultima_gente = False
    last_chist = -99
    lampara_on = valorLampara(GPIO)
    while True: 
            # imagen = imagen - 10
            if (GPIO.input(pir) == 1):
                    GPIO.output(blue_led, 1)
                    if (time.time() - last_chist > 30):
                        playsound('ImagenesDisenio/chist.mp4')
                        last_chist = time.time()
                        # T.start() # Launch created thread
                    if (not ultima_gente and hayUsuario(GPIO)):
                        GPIO.output(green_led, 1)
                        # moverServo(servo)
                        ultima_gente = True
                    # else
                        
            else:
                GPIO.output(blue_led, 0)


            if (ultima_gente and not hayUsuario(GPIO)):
                GPIO.output(green_led, 0)
                ultima_gente = False
            # time.sleep(0.01)

            key = cv2.waitKey(1)
            
            if lamparaPrendida(GPIO, lampara_on) or key == ord('l'): # Inicio del cuadro
                GPIO.output(blue_led, 0)
                GPIO.output(green_led, 0)
                break

