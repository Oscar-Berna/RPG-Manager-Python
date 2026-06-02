class Personaje:
    def __init__(self, nombre, clase, nivel=1, vida=100,
                 vida_maxima=100, ataque=10, defensa=5, id=None):
        self.__id          = id
        self.__nombre      = nombre
        self.__clase       = clase
        self.__nivel       = nivel
        self.__vida        = vida
        self.__vida_maxima = vida_maxima
        self.__ataque      = ataque
        self.__defensa     = defensa

    @property
    def id(self):          return self.__id
    @property
    def nombre(self):      return self.__nombre
    @property
    def clase(self):       return self.__clase
    @property
    def nivel(self):       return self.__nivel
    @property
    def vida(self):        return self.__vida
    @property
    def vida_maxima(self): return self.__vida_maxima
    @property
    def ataque(self):      return self.__ataque
    @property
    def defensa(self):     return self.__defensa

    @nivel.setter
    def nivel(self, n):
        if   n < 1:  self.__nivel = 1
        elif n > 50: self.__nivel = 50
        else:        self.__nivel = n

    def habilidad_especial(self):
        return f'{self.__nombre} usa una habilidad basica'

    def __str__(self):
        return (f'[{self.__clase}] {self.__nombre} Nv{self.__nivel}'
                f' | HP:{self.__vida:.0f}/{self.__vida_maxima:.0f}'
                f' | ATK:{self.__ataque} DEF:{self.__defensa}')


class Guerrero(Personaje):
    def __init__(self, nombre, nivel=1, vida=100, vida_maxima=100,
                 ataque=18, defensa=12, id=None):
        super().__init__(nombre, 'Guerrero', nivel, vida,
                         vida_maxima, ataque, defensa, id)

    def habilidad_especial(self):
        return f'{self.nombre} usa GOLPE DEVASTADOR y causa {self.ataque * 2} de dano!'


class Mago(Personaje):
    def __init__(self, nombre, nivel=1, vida=70, vida_maxima=70,
                 ataque=28, defensa=5, id=None):
        super().__init__(nombre, 'Mago', nivel, vida,
                         vida_maxima, ataque, defensa, id)

    def habilidad_especial(self):
        return f'{self.nombre} lanza BOLA DE FUEGO y causa {self.ataque * 3} de dano!'


class Arquero(Personaje):
    def __init__(self, nombre, nivel=1, vida=85, vida_maxima=85,
                 ataque=22, defensa=8, id=None):
        super().__init__(nombre, 'Arquero', nivel, vida,
                         vida_maxima, ataque, defensa, id)

    def habilidad_especial(self):
        return f'{self.nombre} dispara FLECHA CERTERA y causa {self.ataque * 2.5:.0f} de dano!'
