# from multiprocessing import Process, shared_memory
# from sys import getsizeof
# import time

# def pr1(arg):
#     shm = shared_memory.SharedMemory(arg)
#     shm.buf[4]=6

# def pr2(arg):
#     shm = shared_memory.SharedMemory(arg)
#     shm.buf[2]=6


# if __name__ == '__main__':
#     l = [1, 2, 3, 4, 5]
#     shm = shared_memory.SharedMemory('shm' ,create=True, size=getsizeof(l))
#     p1 = Process(target=pr1, args=('shm',))
#     p2 = Process(target=pr2, args=('shm',))
#     shm.buf = l
#     print(shm.buf)
#     # p_video.join()
#     p2.start()
#     p1.start()
#     # for i in range(5):
#     #     print('hola')
#     #     time.sleep(1)
#     # p_data.join() # wait until acquire_data is done
#     p2.join() # wait also until capture_video is done
#     p1.join()

#     print(shm.buf)
#     # print('paso')

from multiprocessing import Process, Manager

# def myf(myd, pos):
#     myd[pos] = "HELLO WORLD!"

def proc(d, pos):
    d[pos] = "HELLO WORLD!"

if __name__ == '__main__':
    m=Manager()
    locdict=m.dict()
    locdict[2] = "HI BUDDY!"
    pos = '3'

    p = Process(target=proc, args=(locdict, pos,))

    p.start()
    p.join()

    for item in locdict:
        print(item)

    # print(locdict) 