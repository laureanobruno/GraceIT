import RPi.GPIO as GPIO
import time

trig = 23
echo = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)         #Read output from PIR motion sensor
GPIO.setup(echo, GPIO.IN)  

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
    pulso_inicial = time.time()
    while True:
        pulso_inicio = time.time()
        if GPIO.input(echo) == GPIO.HIGH or (time.time() - pulso_inicial > 0.1):
            break

    # El pin ECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo. 
    # En ese momento el sensor pondrá el pin ECHO en bajo.
    # Prodedemos a detectar dicho evento para terminar la medición del tiempo
    
    while True:
        pulso_fin = time.time()
        if GPIO.input(echo) == GPIO.LOW:
            break

    # Tiempo medido en segundos
    duracion = pulso_fin - pulso_inicio

    #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
    distancia = (17150 * duracion)

    return distancia

def hayUsuario():
    filterArray = []
    # 1. TAKING MULTIPLE MEASUREMENTS AND STORE IN AN ARRAY
    for i in range(0,20):
        filterArray.append(medirUltrasonido())
        time.sleep(20/10000)

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
    return distancia_promedio < 201

while True:
    if hayUsuario():
        print("Hay usuario")
    else:
        print("No hay usuario")
    time.sleep(0.5)