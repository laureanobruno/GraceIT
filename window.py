import cv2
from collections import OrderedDict
from funciones import *

from imagenes.agua import Agua
from imagenes.bug import Bug
from imagenes.lampara import Lampara
from imagenes.ojos import Ojos

class Window:

    luz = False
    agua = False

    def __init__(self):
        resize = 1
        full_screen = True

        # Se leen las imagenes
        imagenOrig = cv2.imread(f"./ImagenesDisenio/graceHopper/Grace.jpg", cv2.IMREAD_UNCHANGED)
        self.imagenOrig = imagenOrig
        img_ojos = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-02.png', cv2.IMREAD_UNCHANGED)

        # Dimensiones de la pantalla
        pix_Y = len(imagenOrig)
        pix_X = len(imagenOrig[0])
        dim = [pix_X, pix_Y]

        img_ojos = cargarOjos(resize, img_ojos)


        bug = []
        lamp = []
        
        cargarLamparayBug(lamp, bug, resize * 0.85)

        medio_agua = []
        inicio_agua = []
        final_agua = []
        cargarAgua(inicio_agua, medio_agua, final_agua, pix_X, pix_Y, resize)

        # Posiciones relativas al tamaño de la pantalla
        posInicialOjos = [round(pix_X * 0.3722), round(pix_Y * 0.296)]
        posInicialLamp = [round(pix_X * 0.32), 0]
        posInicialBug = [round(pix_X * 0.803), round(pix_Y * 0.214)]

        # images es un diccionario ordenado según orden de agregado
        #  de clases que contiene a cada imagen que se muestra en pantalla
        images = OrderedDict()
        images['agua'] = Agua(inicio_agua, medio_agua, final_agua, False, [0,0], dim)
        images['ojos'] = Ojos([img_ojos], True, posInicialOjos, dim)
        images['lamp'] = Lampara(lamp, True, posInicialLamp, dim)
        images['bug'] = Bug(bug, False, posInicialBug, dim,1)
        self.images = images

        if (full_screen):
            cv2.namedWindow("Grace", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Grace",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        else:
            cv2.namedWindow("Grace", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Grace", pix_X, pix_Y)

        #hide mouse
        cv2.setMouseCallback("Grace", lambda *args : None)



    def prenderLampara(self):
        self.images['lamp'].encender()
        self.luz = True

    def apagarLampara(self):
        self.images['lamp'].apagar()
        self.images['bug'].reiniciar() # lo devuelve a la posicion inicial y lo oculta
        self.images['ojos'].reiniciar()
        self.luz = False

    def toggleLampara(self):
        if self.luz:
            self.apagarLampara()
        else:
            self.prenderLampara()

    def abrirCanilla(self):
        self.images['agua'].iniciar()
        self.images['bug'].reiniciar()
        self.images['ojos'].reiniciar()
        self.agua = True

    def cerrarCanilla(self):
        self.images['agua'].terminar()


    def mostrarImagen(self):
        if self.images['agua'].terminoAnimacion:
            self.agua = False

        if self.agua:
            self.images['agua'].actuar()
            act_agua = self.images['agua'].getImg()
            imagen = superponerImagenes(act_agua, self.images)
        else:
            imagen = superponerImagenes(self.imagenOrig, self.images)

        if self.luz:
            if not self.agua: # si no hay agua, el bug se mueve
                self.images['bug'].mostrar_bug()
                self.images['bug'].actuar()
                self.images['ojos'].actuar(self.images['bug'].getPos())
        else:   # siempre que no haya luz se pone en gris
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grace", imagen)

    def close(self):
        cv2.destroyAllWindows()
