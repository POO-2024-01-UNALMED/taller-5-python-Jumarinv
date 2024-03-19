from zooAnimales import Animal

class Reptil (Animal):

    listado = []
    iguanas = 0
    serpientes = 0

    def __init__ (self, nombre, edad, habitat, genero, colorEscamas, largoCola):

        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

        Reptil.listado.append(self)

    @classmethod
    def cantidadReptiles (cls):

        return(len(cls.listado))
    
    def movimiento (self):

        return("reptar")
    
    @classmethod
    def crearIguana (cls, nombre, edad, genero):

        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)

        cls.iguanas += 1

        return (iguana)
    
    @classmethod
    def crearSerpiente (cls, nombre, edad, genero):

        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)

        cls.serpientes += 1

        return (serpiente)
    
    @classmethod
    def getSerpientes (cls):

        return (cls.serpientes)
    
    @classmethod
    def getIguanas (cls):

        return (cls.iguanas)
    
    def getColorEscamas (self):

        return (self._colorEscamas)
    
    def getLargoCola (self):

        return (self._largoCola)