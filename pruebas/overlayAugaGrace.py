from email.mime import image
import cv2
import cvzone

def cargarAguayPile(imagenFondo,pix_X, pix_Y, resize):
    for i in range(0,4):


        agua_img = cv2.imread(f"./ImagenesDisenio/Agua/singrace/chorroEnteroInicio/chorro{i+1}.png", cv2.IMREAD_UNCHANGED)
        # cv2.imshow("winname", agua_img)
        # cv2.waitKey(0)
        agua_img = cv2.resize(agua_img, (0,0), agua_img, resize, resize)
        agua_img = cvzone.overlayPNG(imagenFondo, agua_img)
        # print(agua_img.shape)
        cv2.imwrite(f"./ImagenesDisenio/Agua/chorroEnteroInicio/Agua 2-0{i+8}.png", agua_img)

    for i in range(0,18):
        agua_img = cv2.imread(f"./ImagenesDisenio/Agua/singrace/Cascada en movimiento/Cascada movimiento-{i+1}.png", cv2.IMREAD_UNCHANGED)
        agua_img = cv2.resize(agua_img, (0,0), agua_img, resize, resize)
        agua_img = cvzone.overlayPNG(imagenFondo, agua_img)
        # print(agua_img.shape)
        cv2.imwrite(f"./ImagenesDisenio/Agua/Cascada en movimiento/Cascada movimiento-{i+1}.png", agua_img)

    for i in range(0,6):
        pile_img = cv2.imread(f"./ImagenesDisenio/Agua/singrace/Pileta/Pileta-{i+1}.png", cv2.IMREAD_UNCHANGED)
        pile_img = cv2.resize(pile_img, (pix_X,pix_Y), pile_img, resize, resize)
        pile_img = cvzone.overlayPNG(imagenFondo, pile_img)
        # print(pile_img.shape)
        cv2.imwrite(f"./ImagenesDisenio/Agua/Pileta/Pileta-{i+1}.png", agua_img, cv2.IMWRITE_PAM_FORMAT_RGB_ALPHA)

    # for i in range(0,5):
    #     agua_img = cv2.imread(f"./ImagenesDisenio/Agua/fragmentosDeAgua/Agua-0{i+1}.png", cv2.IMREAD_UNCHANGED)
    #     agua_img = cv2.resize(agua_img, (0,0), agua_img, resize, resize)
    #     agua_img = cvzone.overlayPNG(imagenFondo, agua_img)
    #     # print(agua_img.shape)
    #     cv2.imwrite(f"./ImagenesDisenio/Agua/congrace/Agua-0{i+1}.png", agua_img)


grace = cv2.imread('../ImagenesDisenio/graceHopper/Grace.png', cv2.IMREAD_UNCHANGED)
# cv2.imshow(":asdf", grace)
cv2.waitKey(0)
# Dimensiones de la pantalla
pix_Y = len(grace)
pix_X = len(grace[0])
dim = [pix_X, pix_Y]
print(pix_X)
print(pix_Y)

white_bg_img = cv2.imread("../ImagenesDisenio/bg.jpg", cv2.IMREAD_UNCHANGED)
white_bg_img = cv2.resize(white_bg_img, (pix_X,pix_Y))

p = cv2.imread("../ImagenesDisenio/Agua/singrace/Cascada en movimiento/Cascada movimiento-3.png", cv2.IMREAD_UNCHANGED)

t = cvzone.overlayPNG(white_bg_img, p, [0, 0])
cv2.imwrite("../ImagenesDisenio/prueba.png", t)
prueba = cv2.imread("../ImagenesDisenio/prueba.png", cv2.IMREAD_UNCHANGED)
# cv2.imwrite("asdf", img, )

# imagenFondo = cvzone.overlayPNG(white_bg_img, prueba)
cv2.imshow(":asdf", prueba)
cv2.waitKey(0)
# cargarAguayPile(imagenFondo, pix_X, pix_Y, 1)
