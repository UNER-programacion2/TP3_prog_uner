from pizza import Pizza

class MaestroPizzero:

    def __init__(self, nom: str, ordenes: list{ordenes}):
        self.__nombre = nom
        self.__pizzasPorCocinar = []
        self.__pizzasPorEntregar = []
        self.__ordenes = ordenes

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPedido(self, var: str):
        pizza = Pizza(var)
        self.__pizzasPorCocinar.append(pizza)

    def cocinar(self):
        for pizza in self.__pizzasPorCocinar:
            print(self.__nombre + ": cocinando una pizza de " + pizza.obtenerVariedad())
            self.__pizzasPorEntregar.append(pizza)

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
        