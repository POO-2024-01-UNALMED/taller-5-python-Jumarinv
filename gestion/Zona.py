from zooAnimales.animal import *

class Zona ():

    def __init__ (self, nombre = None, zoo = None):

        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

        if zoo != None:
            self._zoo.agregarZonas(self)

    def agregarAnimales (self, animal):

        self._animales.append(animal)

    def cantidadAnimales (self):

        return(len(self._animales))
    
    def getZoo (self):

        return(self._zoo)
    
    def getNombre (self):

        return(self._nombre)
    

