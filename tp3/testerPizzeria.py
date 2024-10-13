from pizzavariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo

class TesterPizzeria:
    def main(self):
        # a. Crea objetos de tipo PizzaVariedad, Pizza, Orden, MaestroPizzero y Mozo
        muzzarella = PizzaVariedad("Muzzarella", 500)
        napolitana = PizzaVariedad("Napolitana", 540)

        pizza1 = Pizza(muzzarella)
        pizza2 = Pizza(napolitana)

        orden1 = Orden(1, [pizza1, pizza2])

        maestro = MaestroPizzero("Nicolas")
        mozo = Mozo("Beatriz")

        # b. Envia  mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.
        maestro.tomarPedido(orden1)
        maestro.cocinar()
        
        # c. Envia los mensajes tomarPizzas y servirPizzas a los objetos de la clase Mozo.
        mozo.tomarPizzas([pizza1, pizza2])
        mozo.servirPizzas()
        
        # d. Muestra la  transición de estados de los objetos de las clases Orden y Pizza.
        print(f"Estado de la Orden {orden1.obtenerNroOrden()}: {orden1.obtenerEstadoOrden()}")
        estados_pizzas = [pizza.obtenerEstado() for pizza in orden1.obtenerPizzas()]
        print(f"Estado de las Pizzas en la Orden {orden1.obtenerNroOrden()}: {estados_pizzas}")

        # e. Muestra y calcula  el total de la orden. 
        total1 = orden1.calcularTotal()
        print(f"Total de la Orden {orden1.obtenerNroOrden()}: {total1}")

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
