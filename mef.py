import cv2
import time
import threading
from playsound import playsound
from window import Window

PERIODO = 16   # 16ms -> 60fps

class MEF():

    win = Window()

    def __init__(self, sensores):
        self.ticks = 0
        self.sensores = sensores
        self.interruptor = sensores.interruptor
        self.canilla = sensores.canilla
        self.movimiento = sensores.movimiento
        self.presencia = sensores.presencia
        self.finish = False
        self.ult_chist = time.time() - 40
        self.ult_persona = time.time() - 40
        self.ejecutar = True
        #threading.Thread(target=self.playAudio).start()

    def sim_sensors(self):                                                      # Simula los sensores en caso de que no estn conectados
        key = cv2.waitKey(PERIODO)
        #if q or ESC are pressed
        if (key == ord('q') or key == 27):
            self.finish = True

        elif key == ord('l'):
            self.interruptor.toggle()

        elif key == ord('a'):
            self.canilla.set()

        elif key == ord('c'):
            self.canilla.reset()

        elif key == ord('m'):
            self.movimiento.set()

        elif key == ord('p'):
            self.presencia.toggle()

    def playAudio(self):
        playsound('ImagenesDisenio/chist.wav')

    def update_image(self):
        tiempoAct = time.time()

        if self.interruptor.has_changed:                                        # Si se prendió o se apagó la luz se enciende esa "flag"
            self.win.toggleLampara()
            self.sensores.toggle_leds()
            if not self.win.luz:
                self.ult_chist = tiempoAct - 40                                 # Si se apaga la luz, se reinicia el contador de chist
                self.ejecutar = True
            self.interruptor.has_changed = False


        if self.canilla.has_changed:                                            # Si se abrió o se cerró la canilla se enciende esa "flag"
            if self.canilla.get():
                self.win.abrirCanilla()
            else:
                self.win.cerrarCanilla()

            self.canilla.has_changed = False

        if ((tiempoAct - self.ult_chist) > 40) and not self.win.luz:
            if self.movimiento.get():
                self.ult_chist = tiempoAct
                self.movimiento.reset()
                threading.Thread(target=self.playAudio).start()                 # Reproduzco el audio en otro hilo
                threading.Thread(target=self.sensores.blink_leds, args=(5,)).start() # Hago parpadear los leds
                self.movimiento.reset()

        # if self.movimiento.get():
        #     if not self.win.luz:                                                # Si se detectó movimiento y la luz está apagada
        #         if (tiempoAct - self.ult_chist) > 40:                           # Si pasaron 40 segundos desde que llamo vuelve a llamar
        #             self.ult_chist = tiempoAct
        #             self.movimiento.reset()
        #             threading.Thread(target=self.playAudio).start()             # Reproduzco el audio en otro hilo
        #             self.sensores.blink_leds(5)                                 # Hago parpadear los leds
        #         else:
        #             self.movimiento.reset()
        #     else:                                                               # si la luz esta prendida se resetea el sensor de movimiento
        #         self.movimiento.reset()


        if self.presencia.get():
            self.ult_persona = tiempoAct
            self.ejecutar = True                                                # Este flag se usa para que lo de abajo solo se ejecute una vez
        elif (self.ejecutar and ((tiempoAct - self.ult_persona) > 20)):         # Si no se detecta presencia por 20 segundos se apaga la luz
            self.win.apagarLampara()
            self.ejecutar = False
        

        self.win.mostrarImagen()            # Muestra la imagen en pantalla con los elementos correspondientes

        return self.finish