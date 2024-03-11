from typing import final
import cv2
import cvzone
from multiprocessing import Manager, Process
import time


def superponerImagenes(img_back, imgs_front):
    final_img = img_back
    for img in imgs_front:
        if (imgs_front[img].mostrarse()):
            img_act = imgs_front[img].getImg()
            pos_act = imgs_front[img].getPos()
            final_img = cvzone.overlayPNG(final_img, img_act, pos_act)

    return final_img

def reiniciarImagenes(images):
    for img in images:
        images[img].reiniciar()

def cargarOjos(resize, img_ojos):
    resize_ojos = resize * 0.6
    img_ojos = cv2.resize(img_ojos, (0, 0), img_ojos, resize_ojos, resize_ojos)
    return img_ojos

def cargarLamparayBug(lamp, bug, resize):
    resize_bug = resize * 0.4
    resize_lamp = resize * 0.65
    for i in range(0, 2):
        img_bug = cv2.imread(f"./ImagenesDisenio/graceHopper/bug{i}.png", cv2.IMREAD_UNCHANGED)
        img_bug = cv2.resize(img_bug, (0, 0), img_bug, resize_bug, resize_bug)
        bug.append(cvzone.rotateImage(img_bug, 180))

        img_lamp = cv2.imread(f"./ImagenesDisenio/graceHopper/lampara{i}.png", cv2.IMREAD_UNCHANGED)
        img_lamp = cv2.resize(img_lamp, (0, 0), img_lamp, resize_lamp, resize_lamp)
        lamp.append(img_lamp)

def cargarAgua(inicio_agua, medio_agua, final_agua, pix_X, pix_Y, resize):

    for i in range(1,29):
        nro_img = f"{i}"
        agua_grace = cv2.imread(f"./ImagenesDisenio/Agua/Grace Hopper - 5-10-23/Inicio/Grace ({nro_img}).jpg")
        inicio_agua.append(agua_grace)

    for i in range(1,28):
        nro_img = f"{i}"
        agua_grace = cv2.imread(f"./ImagenesDisenio/Agua/Grace Hopper - 5-10-23/Loop/Grace ({nro_img}).jpg")
        medio_agua.append(agua_grace)

    for i in range(20,80):
        nro_img = f"{i}"
        agua_grace = cv2.imread(f"./ImagenesDisenio/Agua/Grace Hopper - 5-10-23/Final/Grace ({nro_img}).jpg")
        final_agua.append(agua_grace)