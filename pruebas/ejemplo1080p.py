import cv2
from cv2 import waitKey
import cvzone
from collections import OrderedDict

import numpy as np
from clases import *
    

def superponerImagenes(img_back, imgs_front):
    final_img = img_back
    # cv2.imshow("demostracion", final_img)
    # cv2.waitKey(0)

    for img in imgs_front:
        if (imgs_front[img].mostrarse()):
            img_act = imgs_front[img].getImg()
            pos_act = imgs_front[img].getPos()
            
            # Para el caso del agua!!
            if (len(img_act) < 50):
                for i in range(0, len(img_act)):
                    final_img = cvzone.overlayPNG(final_img, img_act[i], pos_act)
                    # cv2.imshow("demostracion", final_img)
                    # cv2.waitKey(0)
            else:
                final_img = cvzone.overlayPNG(final_img, img_act, pos_act)
                # cv2.imshow("demostracion", final_img)
                # cv2.waitKey(0)
    return final_img

def overlay_fran(img_bg, img_front):
    for pix_X in range(0, len(img_bg)):
        for pix_Y in range(0, len(img_bg[0])):
            bool = (img_front[pix_X][pix_Y][0] == 0) and (img_front[pix_X][pix_Y][0] == 0) and (img_front[pix_X][pix_Y][0] == 0)
            if  not bool:
                img_bg[pix_X][pix_Y] = img_front[pix_X][pix_Y]

    return img_bg

# Se leen las imagenes
grace = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-01.png', cv2.IMREAD_UNCHANGED)
old_pix_X = len(grace[0])
old_pix_Y = len(grace)
grace = cv2.resize(grace, (1080, 1920), grace)

# Dimensiones de la pantalla
pix_Y = len(grace)
pix_X = len(grace[0])

# Proporcion de cambio
propX = pix_X / old_pix_X
propY = pix_Y / old_pix_Y

img_ojos = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-02.png', cv2.IMREAD_UNCHANGED)
img_ojos = cv2.resize(img_ojos, (0,0), img_ojos, propX, propY)

no_bg_img = cv2.imread("./ImagenesDisenio/no_bg_img.png")
no_bg_img = cv2.resize(no_bg_img, (pix_X,pix_Y))
white_bg_img = cv2.imread("./ImagenesDisenio/bg.jpg")
white_bg_img = cv2.resize(white_bg_img, (pix_X, pix_Y))
imagenOrig = white_bg_img
# c = Objeto('prueba', [grace], acciones_lampara)
# c.actuar()
# print('segundo acto')qq
# c.actuar()

# cv

images = OrderedDict()

bug = []
lamp = []
for i in range(0, 2):
    img_bug = cv2.imread(f"./ImagenesDisenio/graceHopper/bug{i}.png", cv2.IMREAD_UNCHANGED)
    img_bug = cv2.resize(img_bug, (0, 0), img_bug, 0.4, 0.4)
    bug.append(cvzone.rotateImage(img_bug, 180))

    img_lamp = cv2.imread(f"./ImagenesDisenio/graceHopper/Grace Hopper-0{6 - i}.png", cv2.IMREAD_UNCHANGED)
    img_lamp = cv2.resize(img_lamp, (0,0), img_lamp, 0.4, 0.4)
    lamp.append(img_lamp)

img_bug = cv2.imread("./ImagenesDisenio/graceHopper/bug quemado.png", cv2.IMREAD_UNCHANGED)
img_bug = cv2.resize(img_bug, (0, 0), img_bug, 0.2, 0.2)
# img_bug = cv2.resize(img_bug, (0, 0), img_bug, 0.20, 0.20)
bug.append(cvzone.rotateImage(img_bug, 180))

agua = []
for i in range(0,4):
    agua_img = cv2.imread(f"./ImagenesDisenio/Agua/chorroEnteroInicio/Agua 2-0{i+8}.png", cv2.IMREAD_UNCHANGED)
    agua_img = cv2.resize(agua_img, (pix_X,pix_Y), agua_img)
    # print(agua_img.shape)
    agua.append(agua_img)
for i in range(0,4):
    agua_img = cv2.imread(f"./ImagenesDisenio/Agua/Cascada en movimiento/Cascada movimiento-{i+1}.png", cv2.IMREAD_UNCHANGED)
    agua_img = cv2.resize(agua_img, (pix_X,pix_Y), agua_img)
    # print(agua_img.shape)
    agua.append(agua_img);
imgs_pile = []
for i in range(0,6):
    pile_img = cv2.imread(f"./ImagenesDisenio/Agua/Pileta/Pileta-{i+1}.png", cv2.IMREAD_UNCHANGED)
    pile_img = cv2.resize(pile_img, (pix_X,pix_Y), pile_img)
    # print(pile_img.shape)
    imgs_pile.append(pile_img);
for i in range(0,5):
    agua_img = cv2.imread(f"./ImagenesDisenio/Agua/fragmentosDeAgua/Agua-0{i+1}.png", cv2.IMREAD_UNCHANGED)
    agua_img = cv2.resize(agua_img, (pix_X,pix_Y), agua_img)
    # print(agua_img.shape)
    agua.append(agua_img);

dim = [pix_X, pix_Y]
print(dim)

posInicialOjos = [round(pix_X * 0.426), round(pix_Y * 0.26)]
# posInicialOjos = [round(pix_X * 0.426), round(pix_Y * 0.27)]
posInicialLamp = [round(pix_X * 0.43), 0]
posInicialBug = [round(pix_X * 0.803), round(pix_Y * 0.214)]

images['agua'] = Agua(agua, imgs_pile, False, [0,0], dim)
images['grace'] = ImgSinAcciones([grace], True, [0,0], dim)
images['ojos'] = Ojos([img_ojos], True, posInicialOjos, dim)
images['lamp'] = Lampara(lamp, True, posInicialLamp, dim)
images['bug'] = Bug(bug, False, posInicialBug, dim,1)

huboCambios = True

while True:
    if huboCambios:
        imagen = superponerImagenes(imagenOrig, images)
        huboCambios = False
    cv2.imshow("Grace", imagen)

    key = cv2.waitKey(50)

    if (images['bug'].mostrarse()):
        huboCambios = images['bug'].getCambios()
        images['bug'].actuar()
    if (images['agua'].mostrarse()):
        images['agua'].actuar();
        huboCambios = images['agua'].getCambios() or huboCambios

    if key == ord('q'):
        break
    elif key == ord('b'):
        huboCambios = True
        images['bug'].cambiarEstado()
    elif key == ord('l'):
        huboCambios = True
        images['lamp'].actuar()
    elif key == ord('a'):
        huboCambios = True
        images['agua'].cambiarEstado()