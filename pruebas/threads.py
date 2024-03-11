import time
import threading as th
import cv2, cvzone
import concurrent.futures



variable = 2

def hola(index, matrix):
    for i in range(0, len(matrix[index])):
        matrix[index][i] *= index


def overlayFran(img_bg, img_front):


    for i in range(len(img_bg)):
        for j in range(len(img_bg[0])):
            img_bg[i][j][0] = img_front[i][j][0]
            img_bg[i][j][1] = img_front[i][j][1]
            img_bg[i][j][2] = img_front[i][j][2]
            # print(img_bg[i][j])
            # print(img_front[i][j])




# print(len(black_bg))




# cv2.imshow("asdf", black_bg)
# cv2.waitKey(0)

# # matrix = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]
 
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     for i in range(0,1920):
#         f = executor.submit(overlayFran, black_bg, grace, i)
#         ths.append(f)

    # t = th.Thread(target=overlayThread, args=(black_bg, grace, i))
    # t.start()

        # for t in ths:
        #     t.join()


black_bg = cv2.imread("../ImagenesDisenio/black_bg.png")


start = time.perf_counter()
grace = cv2.imread("../ImagenesDisenio/graceHopper/Grace.png", cv2.IMREAD_UNCHANGED)
agua = cv2.imread("../ImagenesDisenio/Agua/Cascada en movimiento sin grace/Cascada movimiento-1.png", cv2.IMREAD_UNCHANGED)
# black_bg = cvzone.overlayPNG(black_bg, grace)
# overlayFran(black_bg, grace)
# finish = time.perf_counter()
# print(f"Finished in {round(finish-start,3)} second(s)")

# def overlayThread(start, end, len_img):
#     # print(start)
#     # print(end)
#     print(th.current_thread())
#     for i in range(start, end):
#         for j in range(len_img):
#             black_bg[i][j][0] = grace[i][j][0]
#             black_bg[i][j][1] = grace[i][j][1]
#             black_bg[i][j][2] = grace[i][j][2]

def overlayThread(imgBack, imgFront):
    imgBack = cvzone.overlayPNG(imgBack, imgFront)
    cv2.imshow("asdf", black_bg)
    cv2.waitKey(0)  

end = 160
s = 0
ths = []
# len_bg = len(black_bg[0])
# 
imgs = [grace, agua]
for i in range(0,2):
    t = th.Thread(target=overlayThread, args=(black_bg, imgs[i]))
    t.start()
    ths.append(t)

for t in ths:
    t.join()

finish = time.perf_counter()
# overlayFran(black_bg, grace)
print(f"Finished in {round(finish-start,3)} second(s)")


# finish = time.perf_counter()
# # print(matrix)
# print(f"Finished in {round(finish-start,3)} second(s)")


cv2.imshow("asdf", black_bg)
cv2.waitKey(0)