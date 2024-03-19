from zooAnimales import Animal

class Zona ():

    def __init__ (self, nombre, zoo):

        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

        self._zoo.agregarZonas(self)

    def agregarAnimales (self, animal):

        self._animales.append(animal)

    def cantidadAnimales (self):

        return(len(self._animales))
    
    def getZoo (self):

        return(self._zoo)
    
    def getNombre (self):

        return(self._nombre)
    

