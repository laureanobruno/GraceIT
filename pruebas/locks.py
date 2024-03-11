from multiprocessing import Process, Lock

def sensores(l):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

# def animacion(l):

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()