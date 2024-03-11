from playsound import playsound
import time
# primero = time.time()
# time.sleep(10)
# print(time.time()-primero)
# # playsound('ImagenesDisenio\\graceChistando.mp3')
import cv2
import cvzone

white_bg_img = cv2.imread("./ImagenesDisenio/bg.jpg")
white_bg_img = cv2.resize(white_bg_img, (0,0), white_bg_img, 0.5, 0.5)
black_bg = cv2.imread("./ImagenesDisenio/black_bg.png")
black_bg = cv2.resize(black_bg, (0,0), black_bg, 0.5, 0.5)
fondo = cv2.imread("./ImagenesDisenio/fondo.png", cv2.IMREAD_UNCHANGED)
fondo = cv2.resize(fondo, (0,0), fondo, 0.5, 0.5)
fondo1 = cv2.imread("./ImagenesDisenio/fondo.png")
fondo1 = cv2.resize(fondo1, (0,0), fondo1, 0.5, 0.5)
luz = cv2.imread("./ImagenesDisenio/luzR.png")
luz = cv2.resize(luz, (0,0), luz, 0.5, 0.5)
grace_apagada = cv2.imread("./ImagenesDisenio/graceHopper/grace_apagada.png", cv2.IMREAD_UNCHANGED)
grace_apagada = cv2.resize(grace_apagada, (0,0), grace_apagada, 0.5, 0.5)
gr = cv2.imread("./ImagenesDisenio/graceHopper/Grace.png", cv2.IMREAD_UNCHANGED)
gr = cv2.resize(gr, (0,0), gr, 0.5, 0.5)


overlay = cvzone.overlayPNG(black_bg, fondo, [0,0])
grace = cvzone.overlayPNG(white_bg_img, grace_apagada, [0,0])
gr = cvzone.overlayPNG(white_bg_img, gr)
# overlay = cvzone.overlayPNG(fondo, grace_apagada, [0,0])

# cv2.imshow("GRace", overlay)
cv2.imshow("2", grace)
cv2.waitKey(0)
cv2.imshow("2", gr)
cv2.waitKey(0)