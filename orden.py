from pizza import Pizza
from pizzavariedad import *
class Orden:

    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    
#####<<Constructores>>
    def __init__(self, nroO: int,  pizzas: list[Pizza]):
        self.__nroOrden = nroO
        self.__pizzas = pizzas
        self.__estadoOrden = Orden.ESTADO_INICIAL

        #hola
    #chau

    
#####<<Comandos>>
    #establecerNroOrden(nro: int)
    #establecerPizzas(pizzas: Pizza[])
    #Requiere pizzas ligado
    #establecerEstadoOrden(est: int)
    #Requiere est = Orden.ESTADO_INICIAL o Orden.ESTADO_PARA_ENTREGAR o Orden.ESTADO_ENTREGADA    

  

    def establecerNroOrden(self, nroO: int):
        self.nroO = nroO

    def establecerPizzas(self, pizzas: list[Pizza]):
        self.pizzas = pizzas     

    def establecerEstadoOrden(self, est: int):
        if est not in [Orden.ESTADO_INICIAL, Orden.ESTADO_PARA_ENTREGAR, Orden.ESTADO_ENTREGADA]:
            raise ValueError("Estado inválido.")    
                   
        if self.__estadoOrden == Orden.ESTADO_INICIAL and est == Orden.ESTADO_PARA_ENTREGAR:
            self.__estadoOrden = Orden.ESTADO_PARA_ENTREGAR
        elif self.__estadoOrden == Orden.ESTADO_PARA_ENTREGAR and est == Orden.ESTADO_ENTREGADA:
            self.__estadoOrden = Orden.ESTADO_ENTREGADA
        else:
            raise ValueError(f"No se puede hacer esa transición")      
       #    estadoOrden == Orden.ESTADO_PARA_ENTREGAR
    #ESTADO_ENTREGADA = 3
        


#####<<Consultas>>
    #obtenerNroOrden(): int
    #obtenerPizzas(): Pizza[]
    #obtenerEstadoOrden(): int
    #calcularTotal(): float  

    def obtenerNroOrden(self):
        return self.__nroO
   
    def obtenerPizzas (self): 
        return self.__pizzas

    def obtenerEstadoOrden(self):
        return self.__est


# La consulta calcularTotal debe calcular el costo total de la orden. Esto debe
# hacerse recorriendo los objetos de tipo Pizza ligados a dicha orden y
# acumulando el costo que tiene cada variedad de pizza.
    def calcularTotal(self):

        for pizza in self.pizzas:
            if nroO = s

