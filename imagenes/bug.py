import cvzone
from .imagen import Imagen
import math as m

class Bug(Imagen):
    def __init__(self, imgs, mostrar, pos, dim, direccion):
        super().__init__(imgs, mostrar, pos, dim)
        self.direccion = direccion
        self.t = 0
        self.posInicial = pos
        self.rotada = False
        self.huboCambios = False

    
    def reiniciar(self):
        """ Reinicia el bug a su estado inicial y lo oculta """
        if self.estaRotado():
            self.rotar(180)
        super().reiniciar()
        self.t = 0
        self.posicion = self.posInicial
        self.huboCambios = False
        self.mostrar = False
        self.direccion = 1

    def getCambios(self):
        return self.huboCambios

    def siguiente_imagen(self):
        ant = self.nro_img_act
        if self.nro_img_act == 0:
            self.nro_img_act = 1
        else:
            self.nro_img_act = 0
        #self.nro_img_act = ((self.nro_img_act + 1) % 2)  # 0 o 1
        self.img_act = self.imgs[self.nro_img_act]

        self.huboCambios = ant != self.nro_img_act

    def rotar(self, angulo):
        self.imgs[0] = cvzone.rotateImage(self.imgs[0], angulo)
        self.imgs[1] = cvzone.rotateImage(self.imgs[1], angulo)
        self.rotada = not self.rotada

    def linea(self):
        x = - round(self.t * (self.dimension[0] * 0.027));
        y = round((self.dimension[1] * 0.0005) * x)

        self.t = (self.t+1*self.direccion)
        if (self.t > 10 or self.t <0):
            self.direccion = -self.direccion
            self.rotar(180)

        self.posicion = [self.posInicial[0] +x, self.posInicial[1]+y]

    def seno(self):
        x = -round(self.t * (self.dimension[0] * 0.027))
        y = round(50 * m.sin(self.t))

        self.t = (self.t+0.1) % 50
        self.rotar(self.t)
        self.posicion = [self.posInicial[0] +x, self.posInicial[1]+y]

    def linea_seno(self):
        x = -round(self.t * (self.dimension[0] * 0.027))
        y = round(50 * m.sin(self.t)) + round((self.dimension[1] * 0.0005) * x)

        self.t = (self.t+ (self.dimension[0] * 0.0006) * self.direccion)
        if (self.t >= 12 or self.t <= 0):
            self.rotar(180)
            # self.imgs[0] = self.imgs[2] # quemarlo
            self.direccion = -self.direccion

        self.posicion = [self.posInicial[0] +x, self.posInicial[1]+y]

    def circulo(self):
        x = round(100 * m.cos(self.t))
        y = round(100 * m.sin(self.t))

        if (y<0 and not self.rotada):
            self.rotar(180)
        elif (y>0 and self.rotada):
            self.rotar(180)

        self.t = (self.t+0.1) % 100
        self.posicion = [self.posInicial[0] +x, self.posInicial[1]+y]

    def actuar(self):
        # self.circulo()
        self.linea_seno()
        # self.linea()
        self.siguiente_imagen()
        # pass
        return

    def estaRotado(self):
        return self.rotada

    def mostrar_bug(self):
        self.mostrar = True