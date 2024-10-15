from orden import Orden
from pizza import Pizza

class MaestroPizzero:

#####<<Atributos de instancia>>
    def __init__(self, nom: str):
        self.__nombre = nom
        self.__ordenes = []  
#####<<Comandos>>
    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, orden: Orden):
        if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:  
            self.__ordenes.append(orden)  

    def cocinar(self):
        for orden in self.__ordenes:
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:  
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)  
                for pizza in orden.obtenerPizzas():
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)  

    def entregar(self, orden: Orden):
        pizzasAEntregar = []
        for pizza in orden.obtenerPizzas():
            if pizza.obtenerEstado() == Pizza.ESTADO_COCINADA and len(pizzasAEntregar) < 2:
                pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)  
                pizzasAEntregar.append(pizza)

        if all(p.obtenerEstado() == Pizza.ESTADO_ENTREGADA for p in orden.obtenerPizzas()):
            orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)  

        return pizzasAEntregar  
#####<<Consultas>>
    def obtenerNombre(self):
        return self.__nombre

    def obtenerOrdenes(self):
        return self.__ordenes
