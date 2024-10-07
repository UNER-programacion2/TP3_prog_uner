from pizzavariedad import PizzaVariedad

class Pizza:

    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3


    def __init__(self, var: PizzaVariedad, estado : int):
        self.__variedad = var
        self.__estado = estado

    #comandos 
    def establecerVariedad(self, var: str):
        self.__variedad = var
    
    def establecerEstado(self, est: int ):
        self.__est = est

      #consultas
    def obtenerVariedad(self):
        return self.__variedad

    def obtenerEstado(self):
        return self.__est
    
    def __repr__(self):
        return self.__variedad






# <<Constructores>>
# Pizza(var: PizzaVariedad)
# Requiere var ligado
# <<Comandos>>
# establecerVariedad(var: PizzaVariedad)
# Requiere var ligado
# establecerEstado(est: int)
# <<Consultas>>
# obtenerVariedad(): PizzaVariedad
# obtenerEstado(): int