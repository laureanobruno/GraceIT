from .imagen import Imagen

class Ojos(Imagen):
    def __init__(self, imgs, mostrar, pos, dim):
        super().__init__(imgs, mostrar, pos, dim)
        self.posInicial = pos

    def reiniciar(self):
        self.posicion[0] = self.posInicial[0]
        self.posicion[1] = self.posInicial[1]

    def actuar(self, posBug):

        # Los ojos se mueven al rededor de una circunferencia de radio R en función de la posición del bug.
        # Se cumple que PosNueva = (dist_bug_act / dist_max_bug) * R
        # Luego PosActOjos = PosInicial + PosNueva
        # Esto es lo que representan las variables diferencia_x y diferencia_y en ambas dimensiones.
        # La expresion (self.dimension[0] * 0.0174) es asi porque es proporcional al tamaño de la pantalla. Quiere decir R = self.dimension[0] * 0.0174
        
        diferencia_x = round((posBug[0] - self.posInicial[0]) / (self.dimension[0] * 0.574) * (self.dimension[0] * 0.0174))
        diferencia_y = round((posBug[1] - self.posInicial[1]) / (self.dimension[1] * 0.741) * (self.dimension[0] * 0.0174))
        self.posicion = [self.posInicial[0] + diferencia_x, self.posInicial[1] + diferencia_y]
        
        return