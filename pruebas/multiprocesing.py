from multiprocessing import Process
import time

def acquire_data(arg):
    for i in range(5):
        print('acquiring data: {}'.format(arg))
        time.sleep(1)

def capture_video():
    return
    for i in range(5):
        print('capturing video')
        time.sleep(1)
    # while True:
    #     pass


if __name__ == '__main__':
    # p_data = Process(target=acquire_data, args=('foo',))
    p_video = Process(target=capture_video)
    # p_video.join()
    # p_data.start()
    p_video.start()
    for i in range(5):
        print('hola')
        time.sleep(1)
    # p_data.join() # wait until acquire_data is done
    p_video.join() # wait also until capture_video is done
    print('paso')
    # print('paso')