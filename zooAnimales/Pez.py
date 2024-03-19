from zooAnimales import Animal

class Pez (Animal):

    listado = []
    salmones = 0
    bacalaos = 0

    def __init__ (self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):

        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

        Pez.listado.append(self)

    @classmethod
    def cantidadPeces (cls):

        return(len(cls.listado))
    
    def movimiento (self):

        return("nadar")

    @classmethod
    def crearSalmon (cls, nombre, edad, genero):

        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)

        cls.salmones += 1

        return (salmon)
    
    @classmethod
    def crearBacalao (cls, nombre, edad, genero):

        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)

        cls.bacalaos += 1

        return (bacalao)

    @classmethod
    def getSalmones (cls):

        return (cls.salmones)
    
    @classmethod
    def getBacalaos (cls):

        return (cls.bacalaos)
    
    def getColorEscamas (self):

        return (self._colorEscamas)
    
    def getCantidadAletas (self):

        return (self._cantidadAletas)