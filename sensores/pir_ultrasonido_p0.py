import RPi.GPIO as GPIO
import time

from numpy import True_

pir = 12
trig = 23
echo = 24
green_led = 16
blue_led = 20

def setup():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # GPIO.cleanup()

    GPIO.setup(pir, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)         #Read output from PIR motion sensor
    GPIO.setup(echo, GPIO.IN)        
    GPIO.setup(green_led, GPIO.OUT)
    GPIO.setup(blue_led, GPIO.OUT)

    GPIO.output(blue_led, 0)
    GPIO.output(green_led, 0)

def loop():
    ultima_gente = False
    while True:
        if (GPIO.input(pir) == 1):
            GPIO.output(blue_led, 1)
            if (not ultima_gente and hayGente()):
                GPIO.output(green_led, 1)
                ultima_gente = True
        else:
            GPIO.output(blue_led, 0)


        if (ultima_gente and not hayGente()):
            GPIO.output(green_led, 0)
            ultima_gente = False
        time.sleep(0.01)

def medirUltrasonido():
    # Ponemos en bajo el pin TRIG y después esperamos 0.5 seg para que el transductor se estabilice
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.000001)

    #Ponemos en alto el pin TRIG esperamos 10 uS antes de ponerlo en bajo
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)

    # En este momento el sensor envía 8 pulsos ultrasónicos de 40kHz y coloca su pin ECHO en alto
    # Debemos detectar dicho evento para iniciar la medición del tiempo
    
    while True:
        pulso_inicio = time.time()
        print("1er while")
        if GPIO.input(echo) == GPIO.HIGH:
            break

    # El pin ECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo. 
    # En ese momento el sensor pondrá el pin ECHO en bajo.
    # Prodedemos a detectar dicho evento para terminar la medición del tiempo
    
    while True:
        pulso_fin = time.time()
        print("2do while")
        if GPIO.input(echo) == GPIO.LOW:
            break

    # Tiempo medido en segundos
    duracion = pulso_fin - pulso_inicio

    #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
    distancia = (17150 * duracion)
 
    return distancia

def hayGente():
    filterArray = []
    # 1. TAKING MULTIPLE MEASUREMENTS AND STORE IN AN ARRAY
    for i in range(0,20):
        filterArray.append(medirUltrasonido())
        time.sleep(20/1000)

    # 2. SORTING THE ARRAY IN ASCENDING ORDER
    filterArray.sort()
    # for i in range (0,19):
    #     for j in range(i+1, 20):
    #         if (filterArray[i] > filterArray[j]):
    #             swap = filterArray[i]
    #             filterArray[i] = filterArray[j]
    #             filterArray[j] = swap

    # 3. FILTERING NOISE
    # + the five smallest samples are considered as noise -> ignore it
    # + the five biggest  samples are considered as noise -> ignore it
    # ----------------------------------------------------------------
    # => get average of the 10 
    sum = 0
    for sample in range(5, 15):
        sum += filterArray[sample]

    distancia_promedio = sum/10
    # print(distancia_promedio)
    return distancia_promedio < 150

def main():
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Terminado por teclado")
    finally:
        GPIO.cleanup()

main()