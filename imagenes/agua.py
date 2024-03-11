from .imagen import *

class Agua(Imagen):
    def __init__(self, imgs_inicio, imgs, imgs_final, mostrar, pos, dim):
        super().__init__(imgs, mostrar, pos, dim)
        self.seLleno = False

        self.imgs_final = imgs_final
        self.imgs_inicio = imgs_inicio
        self.nro_fin = 0
        self.nro_inicio = 0
        self.nro_medio = 0

        self.terminarAnimacion = False
        self.terminoAnimacion = False

        self.mostrarFin = False
        self.mostrarInicio = False
        self.mostrarMedio = False

        self.huboCambios = False
        self.img_act = imgs_inicio[0]

    def reiniciar(self):
        super().reiniciar()

        self.nro_fin = 0
        self.nro_inicio = 0
        self.nro_medio = 0
        self.huboCambios = False
        self.mostrar = False

        self.terminarAnimacion = False
        self.terminoAnimacion = False

        self.mostrarFin = False
        self.mostrarInicio = False
        self.mostrarMedio = False

        self.huboCambios = False
        self.img_act = self.imgs_inicio[0]

    def iniciar(self):
        self.mostrarInicio = True
        self.terminarAnimacion = False
        self.terminoAnimacion = False
        self.nro_inicio = 0

    def terminar(self):
        self.terminarAnimacion = True

    def actuar(self):
        
        if self.mostrarInicio:
            self.nro_inicio += 1
            if self.nro_inicio == len(self.imgs_inicio):    # termino el inicio
                self.mostrarInicio = False
                self.mostrarMedio = True
                self.nro_inicio = 0
            else:
                self.img_act = self.imgs_inicio[self.nro_inicio]
        
        elif self.mostrarMedio:
            self.nro_medio += 1
            if self.nro_medio == len(self.imgs):            # termino el medio
                self.mostrarMedio = True
                # si se cerro la canilla se va al final de la animacion, si no vuelve a arrancar
                if self.terminarAnimacion:
                    self.mostrarMedio = False
                    self.mostrarFin = True
                self.nro_medio = 0
            else:
                self.img_act = self.imgs[self.nro_medio]
        
        elif self.mostrarFin:
            self.nro_fin += 1
            if self.nro_fin == len(self.imgs_final):        # termino la animacion
                self.mostrarFin = False
                self.mostrarMedio = False
                self.terminoAnimacion = True
                self.nro_fin = 0
            else:
                self.img_act = self.imgs_final[self.nro_fin]

    def terminoLaAnimacion(self):
        return self.terminoAnimacion

    def getCambios(self):
        return self.huboCambios
