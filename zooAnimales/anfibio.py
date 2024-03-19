from zooAnimales.animal import Animal

class Anfibio (Animal):

    listado = []
    ranas = 0
    salamandras = 0

    def __init__ (self, nombre, edad, habitat, genero, colorPiel, venenoso):

        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

        Anfibio.listado.append(self)
    
    @classmethod
    def cantidadAnfibios (cls):

        return(len(cls.listado))
    
    def movimiento (self):

        return("saltar")

    @classmethod
    def crearSalamandra (cls, nombre, edad, genero):

        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

        cls.salamandras += 1

        return (salamandra)
    
    @classmethod
    def crearRana (cls, nombre, edad, genero):

        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)

        cls.ranas += 1

        return (rana)
    
    @classmethod
    def getRanas (cls):
        
        return (cls.ranas)
    
    @classmethod
    def getSalamandras (cls):

        return(cls.salamandras)
    
    def getColorPiel (self):

        return (self._colorPiel)
    
    def isVenenoso (self):

        return (self._venenoso)