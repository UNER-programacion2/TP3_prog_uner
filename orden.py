from pizza import Pizza
from pizzavariedad import *


class Orden:

    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    
#####<<Constructores>>
    def __init__(self, nro: int,  pizzas: list[Pizza]):
        self.__nroOrden = nro
        self.__pizzas = pizzas
        self.__estadoOrden = Orden.ESTADO_INICIAL

#####<<Comandos>>
    def establecerNroOrden(self, nroO: int):
        self.nroOrden= nroO

    def establecerPizzas(self, pizzas: list[Pizza]):
        self.pizzas = pizzas     

    def establecerEstadoOrden(self, est: int):
        if est not in [Orden.ESTADO_INICIAL, Orden.ESTADO_PARA_ENTREGAR, Orden.ESTADO_ENTREGADA]:
            raise ValueError("Estado no válido.")    
            
        if self.__estadoOrden == Orden.ESTADO_INICIAL and est == Orden.ESTADO_PARA_ENTREGAR:
            self.__estadoOrden = Orden.ESTADO_PARA_ENTREGAR
        elif self.__estadoOrden == Orden.ESTADO_PARA_ENTREGAR and est == Orden.ESTADO_ENTREGADA:
            self.__estadoOrden = Orden.ESTADO_ENTREGADA
        else:
            raise ValueError("No se puede hacer esa transición")      
    #    estadoOrden == Orden.ESTADO_PARA_ENTREGAR
    #ESTADO_ENTREGADA = 3
        

#####<<Consultas>>

    def obtenerNroOrden(self):
        return self.__nroOrden

    def obtenerPizzas (self): 
        return self.__pizzas

    def obtenerEstadoOrden(self):
        return self.__estadoOrden

    def calcularTotal(self):
        total = 0
        for pizza in self.__pizzas:
            # Accedemos al precio de la variedad de cada pizza
            preTotal = pizza.obtenerPrecio()
            total += preTotal
        return total

        
 ######EJEMPLO PASAR A TESTER       
# ejemplo = PizzaVariedad("Muzzarella", 500) 
# ejempl2 = PizzaVariedad("Napolitana", 540)
# orden = Orden(1, [ejempl2, ejemplo])
# print(f"Número de Orden: {orden.obtenerNroOrden()}")
# print(f"Pizzas en la Orden: {[pizza.obtenerNombreVariedad() for pizza in orden.obtenerPizzas()]}")
# print(f"Total de la Orden: {orden.calcularTotal()}")

 




