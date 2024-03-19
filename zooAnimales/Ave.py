from zooAnimales.animal import Animal

class Ave (Animal):

    listado = []
    halcones = 0
    aguilas = 0

    def __init__ (self, nombre, edad, habitat, genero, colorPlumas):

        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

        Ave.listado.append(self)

    @classmethod
    def cantidadAves (cls):

        return(len(cls.listado))
    
    def movimiento (self):

        return ("volar")
    
    @classmethod
    def crearHalcon (cls, nombre, edad, genero):

        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")

        cls.halcones += 1

        return (halcon)
    
    @classmethod
    def crearAguila (cls, nombre, edad, genero):

        aguilas = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")

        cls.aguilas += 1

        return (aguilas)
    

    @classmethod
    def getHalcones (cls):

        return (cls.halcones)
    
    @classmethod
    def getAguilas (cls):

        return (cls.aguilas)
    
    def getColorPlumas (self):

        return (self._colorPlumas)








