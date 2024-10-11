from orden import Orden
from pizza import Pizza


class MaestroPizzero:
    def __init__(self, nom: str):
        self.__nombre = nom
        self.__ordenes = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, orden : Orden):
        Orden.obtenerEstadoOrden(Orden.ESTADO_INICIAL)
        self.__ordenes.append(orden)

    def cocinar(self):
        for pizza in self.__pizzasPorCocinar:
            print(self.__nombre + ": cocinando una pizza de " + pizza.obtenerVariedad())
            self.__pizzasPorEntregar.append(pizza)
#########VER SI SE PUEDE USAR EL APEND, O SI SE DEBE USAR EL REMOVE

    def entregar(self, pizzas: int):
        pizzasAEntregar = []
        i = 0
        for pizza in self.__pizzasPorEntregar:
            pizzasAEntregar.append(pizza)
            self.__pizzasPorEntregar.remove(pizza)
            i += 1
            if i == pizzas:
                break
        return pizzasAEntregar

    def obtenerNombre(self):
        return self.__nombre

    def obtenerOrdenes(self):
        return self.__ordenes
    
    def obtenerPizzasPorCocinar(self):
        return self.__pizzasPorCocinar
    
    def obtenerPizzasPorEntregar(self):
        return self.__pizzasPorEntregar




#ESTE ES EL DE COPILOT 
""" class MaestroPizzero:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ordenes = []

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def tomar_pedido(self, orden):
        if Orden.establecerEstadoOrden == Orden.ESTADO_INICIAL:
            self.__ordenes.append(orden)

    def cocinar(self):
        for orden in self.__ordenes:
            if orden.obtener_estado_orden() == Orden.ESTADO_INICIAL:
                orden.establecer_estado_orden(Orden.ESTADO_PARA_ENTREGAR)
                for pizza in orden.obtener_pizzas():
                    pizza.establecer_estado(Pizza.ESTADO_COCINADA)

    def entregar(self, orden):
        if orden.obtener_estado_orden() == Orden.ESTADO_PARA_ENTREGAR:
            pizzas_entregadas = []
            for pizza in orden.obtener_pizzas():
                if len(pizzas_entregadas) < 2 and pizza.obtener_estado() == Pizza.ESTADO_COCINADA:
                    pizza.establecer_estado(Pizza.ESTADO_ENTREGADA)
                    pizzas_entregadas.append(pizza)
            if all(pizza.obtener_estado() == Pizza.ESTADO_ENTREGADA for pizza in orden.obtener_pizzas()):
                orden.establecer_estado_orden(Orden.ESTADO_ENTREGADA)
            return pizzas_entregadas

    def obtener_nombre(self):
        return self.__nombre

    def obtener_ordenes(self):
        return self.__ordenes
 """
 