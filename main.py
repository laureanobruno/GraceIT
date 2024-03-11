from mef import MEF
from sensores.sensores import Sensores
import threading
import time

def hilo_sensores(sensores):
    while True:
        sensores.read()
        time.sleep(0.3)

if __name__ == '__main__':

    sensores = Sensores()
    mef = MEF(sensores)

    finish = False 

    threading.Thread(target=hilo_sensores, args=(sensores,)).start()

    while not finish:
        mef.sim_sensors()
        finish = mef.update_image()

    mef.win.close()
