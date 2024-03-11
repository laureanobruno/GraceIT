from multiprocessing.connection import wait
import cv2
from cv2 import waitKey
import cvzone
from collections import OrderedDict

def superponerImagenes(img_back, imgs_front):
    final_img = img_back
    for img in imgs_front:
        if (images[img][2]):
            final_img = cvzone.overlayPNG(final_img, images[img][0], images[img][1])
    return final_img


# Se leen las imagenes
grace = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-01.png')
grace = cv2.resize(grace, (0, 0), grace, 0.35, 0.35)
ojos = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-02.png', cv2.IMREAD_UNCHANGED)
ojos = cv2.resize(ojos, (0, 0), ojos, 0.35, 0.35)

agua = []
for i in range(0,5):
    agua_img = cv2.imread(f"./ImagenesDisenio/Agua/fragmentosDeAgua/Agua-0{i+1}.png", cv2.IMREAD_UNCHANGED)
    agua_img = cv2.resize(agua_img, (0,0), agua_img, 0.4, 0.4)
    # cv2.imshow("agua", agua_img)
    # cv2.waitKey(0)
    agua.append(agua_img);

pile = []
for i in range(0,6):
    pile_img = cv2.imread(f"./ImagenesDisenio/Agua/Pileta/Pileta-{i+1}.png", cv2.IMREAD_UNCHANGED)
    pile_img = cv2.resize(pile_img, (747,933), pile_img, 0.45, 0.45)
    # cv2.imshow("agua", pile_img)
    # cv2.waitKey(0)
    pile.append(pile_img);

images = OrderedDict()

# imagenOrig = cvzone.overlayPNG(grace, ojos, [316, 240])
imagenOrig = grace

# Dimensiones de la pantalla
pix_Y = len(imagenOrig)
pix_X = len(imagenOrig[0])

print(pix_X)
print(pix_Y)

posInicialOjos = [round(pix_X * 0.426), round(pix_Y * 0.258)]

images['ojos'] = [ojos, posInicialOjos, True]
images['agua'] = [agua[0], [0,0], True]
images['pile'] = [pile[0], [0,0], False]

huboCambios = True
i_agua = 1
i_pile = 0

while True:
    if huboCambios:
        imagen = superponerImagenes(imagenOrig, images)
        # huboCambios = False
    cv2.imshow("Grace", imagen)

    if (images['agua'][2] == True):

        if (i_agua == 5):
            images['agua'][2] = False
            images['pile'][2] = True
        else: 
            images['agua'][0] = agua[i_agua]
            i_agua = (i_agua + 1)
            key = waitKey(100)

    if (images['pile'][2] == True):
        if (i_pile < 6):
            images['pile'][0] = pile[i_pile]
            i_pile = (i_pile + 1)
            huboCambios = True
            key = waitKey(130)

    key = waitKey(50)
    if key == ord('q'):
        break