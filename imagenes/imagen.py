#from cv2 import rotate
from abc import ABC, abstractmethod
import math as m

from multiprocessing import Manager, Process

# la posicion[0] es x
# la posicion[1] es y

class Imagen(ABC):

    # Imagen es una clase abstracta que contiene los atributos y metodos basicos de todo
    # elemento que se quiere mostrar en pantalla.
        # imgs: lista de imagenes del objeto
        # img_act: imagen actual a mostrar
        # nro_img_act: numero de imagen actual en la lista de imagenes
        # posicion: posicion en pantalla
        # dimension: dimension de la pantalla
    
    def __init__(self, imgs, mostrar, pos, dim):
        self.imgs = imgs
        self.img_act = imgs[0]
        self.nro_img_act = 0
        self.mostrar = mostrar
        self.posicion = pos
        self.dimension = dim

    @abstractmethod
    def actuar(self, *args):
        pass

    def reiniciar(self):
        self.img_act = self.imgs[0]
        self.nro_img_act = 0

    def mostrarse(self):
        return self.mostrar

    def cambiarEstado(self):
        self.mostrar = not self.mostrar

    def getPos(self):
        return self.posicion

    def getPosAsDict(self):
        return {'x': self.posicion[0], 'y': self.posicion[1]}

    def getImg(self):
        return self.img_act
