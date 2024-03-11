import cv2
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
grace = cv2.resize(grace, (0, 0), grace, 0.5, 0.5)
ojos = cv2.imread('./ImagenesDisenio/graceHopper/Grace Hopper-02.png', cv2.IMREAD_UNCHANGED)
ojos = cv2.resize(ojos, (0, 0), ojos, 0.5, 0.5)

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

# imagenOrig = cvzone.overlayPNG(grace, ojos, [316, 240])
imagenOrig = grace
imagen0 = cvzone.overlayPNG(imagenOrig, lamp[0], [315, 0])

# Dimensiones de la pantalla
pix_Y = len(imagenOrig)
pix_X = len(imagenOrig[0])

print(pix_X)
print(pix_Y)

posInicialOjos = [round(pix_X * 0.426), round(pix_Y * 0.258)]
posInicialLamp = [round(pix_Y * 0.35), 0]

images['lamp'] = [lamp[0], posInicialLamp, True]
images['bug'] = [bug[0], [999, 999], False]
images['ojos'] = [ojos, posInicialOjos, True]
# print(images['bug'][2])

hayBug = False
lampOn = False
i_bug = 0
i_lamp = 0


# Posiciones bug
pos_bug_x = []
pos_bug_y = []
avanzar = 1

x = round(pix_X * 0.803)
y = round(pix_Y * 0.214)
for i in range(0, 51):
    x -= round(pix_X * 0.007)
    y -= round(pix_Y * 0.00321)
    pos_bug_x.append(x)
    pos_bug_y.append(y)

# avanzar = True
j = 1
j2 = 0

huboCambios = True

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
        images['bug'][2] = not images['bug'][2] 
        # Se mira el bug
        if images['bug'][2]:
            images['ojos'][1] = [round(pix_X * 0.435), round(pix_Y * 0.257)]
        else:
            images['ojos'][1] = posInicialOjos

        
    elif key == ord('l'):
        huboCambios = True
        i_lamp = (i_lamp + 1) % 2
        images['lamp'][0] = lamp[i_lamp]

    if images['bug'][2]:
        huboCambios = True

        images['bug'][0] = bug[i_bug]
        images['bug'][1] = [pos_bug_x[j], pos_bug_y[j]]  

        # images['ojos'][1] = [321 - avanzar * round( 5 * j2 / 49), 240 ]

        # print(images['ojos'][1])
        if (j % 10 == 0):
            images['ojos'][1] = [images['ojos'][1][0] - avanzar, images['ojos'][1][1] - avanzar] 

        if j == 0:
            avanzar = 1
            bug[0] = cvzone.rotateImage(bug[0], 180)
            bug[1] = cvzone.rotateImage(bug[1], 180)
        elif j == 50:
            avanzar = -1
            bug[0] = cvzone.rotateImage(bug[0], 180)
            bug[1] = cvzone.rotateImage(bug[1], 180)

        j += avanzar
        
        # j2 = (j2 + 1) % 49

        i_bug = (i_bug + 1) % 2