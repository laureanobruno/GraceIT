from sensores.sensor import Sensor
import RPi.GPIO as GPIO
import time

pir = 12
trig = 23
echo = 24
green_led = 16
lamp = 25
pin_3v = 2
leds = 20
s_canilla = 18

luces = 0

class Sensores:

    def __init__(self):
        self.ult_medicion = 0
        self.interruptor = Sensor()
        self.canilla = Sensor()
        self.movimiento = Sensor()
        self.presencia = Sensor()
        self.configurarGPIO()

    def reset(self):
        self.interruptor.reset()
        self.movimiento.reset()
        self.presencia.reset()

    def configurarGPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(pir, GPIO.IN)
        GPIO.setup(trig, GPIO.OUT)         #Read output from PIR motion sensor
        GPIO.setup(echo, GPIO.IN)
        GPIO.setup(leds, GPIO.OUT)
        GPIO.setup(s_canilla, GPIO.IN)
        GPIO.setup(lamp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin_3v, GPIO.OUT)

        GPIO.output(leds, 0)
        GPIO.output(pin_3v, 1)

        return GPIO

    def medirUltrasonido(self):
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
    
    def hayUsuario(self):
        filterArray = []
        for i in range(0,20):
            filterArray.append(self.medirUltrasonido())
            time.sleep(20/10000)
        filterArray.sort()
        sum = 0
        for sample in range(5, 15):
            sum += filterArray[sample]

        distancia_promedio = sum/10
        return distancia_promedio < 201
    
    def blink_leds(self, cant):
        for i in range(cant):
            GPIO.output(leds, 1)
            time.sleep(0.1)
            GPIO.output(leds, 0)
            time.sleep(0.1)
        global luces
        luces = 0

    def toggle_leds(self):
        global luces
        luces = not luces
        GPIO.output(leds, luces)

    def read(self):
        self.interruptor.set_value(GPIO.input(lamp))
        self.canilla.set_value(GPIO.input(s_canilla))
        self.movimiento.set_value(GPIO.input(pir))
        if not self.presencia.get():
            self.movimiento.set_value(GPIO.input(pir))
        if time.time() - self.ult_medicion > 10:
            aux = self.hayUsuario()
            self.presencia.set_value(aux)
            self.ult_medicion = time.time()

