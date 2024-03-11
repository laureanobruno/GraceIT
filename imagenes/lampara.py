from .imagen import Imagen

class Lampara(Imagen):
    def actuar(self):
        self.nro_img_act = (self.nro_img_act + 1) % len(self.imgs)
        self.img_act = self.imgs[self.nro_img_act]

    def encender(self):
        self.nro_img_act = 1
        self.img_act = self.imgs[self.nro_img_act]

    def apagar(self):
        self.nro_img_act = 0
        self.img_act = self.imgs[self.nro_img_act]