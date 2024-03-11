import cv2
from cv2 import waitKey
from math import sqrt
import cvzone
from collections import OrderedDict

class Objeto:
    def __init__(self, name, imgs, mostrado, pos, dim, comportamiento=None, direccion=None):
        self.name = name
        self.imgs = imgs
        self.img_act = imgs[0]
        self.nro_img_act = 0
        self.mostrar = mostrado
        self.comportamiento = comportamiento
        self.posicion = pos
        self.posicionInicial = pos
        self.dimension = dim
        self.direccion = direccion
  
    def actuar(self, *args):
        self.comportamiento(self, args)

    def mostrarse(self):
        return self.mostrar

    def cambiarEstado(self):
        self.mostrar = not self.mostrar

    def getPos(self):
        return self.posicion
    
    def getImg(self):
        return self.img_act

def acciones_bug(self, *args):
    self.nro_img_act = (self.nro_img_act + 1) % 2
    self.img_act = self.imgs[self.nro_img_act]

    delta_x = round(self.dimension[0] * 0.004) * self.direccion
    self.posicion[0] -= delta_x
    # self.posicion[1] -= round(self.dimension[1] * 0.0025) * self.direccion
    # y = round(sqrt(4-pow(self.posicion[0], 2)))
    # print(y)

    posLamp = args[0][0]
    if (self.posicion[0] <= posLamp[0] - delta_x) or (self.posicion[1] < posLamp[1]):
        self.posicion = self.posicionInicial
        self.direccion = -self.direccion
        self.imgs[0] = cvzone.rotateImage(self.imgs[0], 180)
        self.imgs[1] = cvzone.rotateImage(self.imgs[1], 180)

def acciones_lampara(self, *args):
    self.nro_img_act = (self.nro_img_act + 1) % len(self.imgs)
    self.img_act = self.imgs[self.nro_img_act]

def acciones_ojos(self, *args):
    pass

def superponerImagenes(img_back, imgs_front):
    final_img = img_back
    for img in imgs_front:
        if (imgs_front[img].mostrarse()):
            final_img = cvzone.overlayPNG(final_img, imgs_front[img].getImg(), imgs_front[img].getPos())
    return final_img


# Se leen las imagenes
grace = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-01.png')
grace = cv2.resize(grace, (0, 0), grace, 0.35, 0.35)
img_ojos = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-02.png', cv2.IMREAD_UNCHANGED)
img_ojos = cv2.resize(img_ojos, (0, 0), img_ojos, 0.35, 0.35)

images = OrderedDict()

bug = []
lamp = []
for i in range(0, 2):
    img_bug = cv2.imread(f"./ImagenesDisenio/graceHopper/bug{i}.png", cv2.IMREAD_UNCHANGED)
    img_bug = cv2.resize(img_bug, (0, 0), img_bug, 0.20, 0.20)
    bug.append(cvzone.rotateImage(img_bug, 180))

    img_lamp = cv2.imread(f"./ImagenesDisenio/graceHopper/Grace Hopper-0{6 - i}.png", cv2.IMREAD_UNCHANGED)
    img_lamp = cv2.resize(img_lamp, (0, 0), img_lamp, 0.22, 0.22)
    lamp.append(img_lamp)

img_bug = cv2.imread("./ImagenesDisenio/graceHopper/bug quemado.png")
img_bug = cv2.resize(img_bug, (0, 0), img_bug, 0.20, 0.20)
bug.append(cvzone.rotateImage(img_bug, 180))



imagenOrig = grace

# Dimensiones de la pantalla
pix_Y = len(imagenOrig)
pix_X = len(imagenOrig[0])

dim = [pix_X, pix_Y]

posInicialOjos = [round(pix_X * 0.426), round(pix_Y * 0.258)]
posInicialLamp = [round(pix_X * 0.45), 0]
print(posInicialLamp[1] - posInicialOjos[1])
posInicialBug = [round(pix_X * 0.45 + pix_Y * 0.258), round(pix_Y * 0.258)] #round(pix_Y * 0.214)
print(round(pix_X * 0.45) + round(pix_Y * 0.258))
print(pix_Y)

images['ojos'] = Objeto('ojos', [img_ojos], True, posInicialOjos, dim)
images['lamp'] = Objeto('lampara', lamp, True, posInicialLamp, dim, acciones_lampara)
images['bug'] = Objeto('bug', bug, False, posInicialBug, dim, acciones_bug, 1)

huboCambios = True

for i in range(0,500):
    imagenOrig[100, i] = [255,1,1]
    imagenOrig[i, 100] = [1,255,1]

while True:
    if huboCambios:
        imagen = superponerImagenes(imagenOrig, images)
        huboCambios = False
    cv2.imshow("Grace", imagen)

    key = cv2.waitKey(50)
    if key == ord('q'):
        break
    elif key == ord('b'):
        huboCambios = True
        images['bug'].cambiarEstado()

    elif key == ord('l'):
        huboCambios = True
        images['lamp'].actuar() 

    if (images['bug'].mostrarse()):
        huboCambios = True

        posicion = images['bug'].getPos()
        x =(posicion[0]-round(pix_X * 0.45))
        print(x);   
        y = round(sqrt(pow(round(pix_Y * 0.258), 2)- pow(round(pix_Y * 0.258)-x,2)) )
        imagenOrig[y,posicion[0]] = [255,1,1]

        images['bug'].actuar(images['lamp'].getPos())