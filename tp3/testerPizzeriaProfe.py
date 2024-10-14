from maestropizzero import MaestroPizzero
from mozo import Mozo
from orden import Orden
from pizzavariedad import PizzaVariedad
from pizza import Pizza


class TesterPizzeria:

    def main(self):
        muzza = PizzaVariedad("Muzzarella", 7000.00)
        fugazetta = PizzaVariedad("Fugazetta", 7500.00)
        napolitana = PizzaVariedad("Napolitana", 7500.00)
        rucula = PizzaVariedad("Rucula y Crudo", 9000.00)
        calabresa = PizzaVariedad("Calabresa", 8200.00)
        provolone = PizzaVariedad("Provolone", 8400.00)
        roqueynuez = PizzaVariedad("Roquefort y Nuez", 9000.00)

        pizza1 = Pizza(muzza)
        pizza2 = Pizza(fugazetta)
        pizza3 = Pizza(napolitana)
        pizza4 = Pizza(rucula)
        pizza5 = Pizza(calabresa)
        pizza6 = Pizza(provolone)
        pizza7 = Pizza(roqueynuez)
        pizza8 = Pizza(muzza)
        pizza9 = Pizza(fugazetta)
        pizza10 = Pizza(fugazetta)
        pizza11 = Pizza(rucula)
        pizza12 = Pizza(napolitana)
        pizza13 = Pizza(rucula)
        pizza14 = Pizza(provolone)
        pizza15 = Pizza(provolone)
        pizza16 = Pizza(calabresa)

        orden1 = Orden(1, [pizza1, pizza10])
        orden2 = Orden(2, [pizza2, pizza11])
        orden3 = Orden(3, [pizza3, pizza12, pizza13])
        orden4 = Orden(4, [pizza4, pizza14])
        orden5 = Orden(5, [pizza5, pizza6, pizza7])
        orden6 = Orden(6, [pizza8, pizza9, pizza15, pizza16])
        ordenes = [orden1, orden2, orden3, orden4, orden5, orden6]
        
        pipo = MaestroPizzero("Pipo")
        nico = Mozo("Nico")
        juan = Mozo("Juan")

        print('----------------------------------------\nPizzeria de Don Pipo\n----------------------------------------')

        print("\nTomando pedidos...")
        for orden in ordenes:
            print("Pipo tomando pedido #" + str(orden.obtenerNroOrden()))
            pipo.tomarPedido(orden)

        self.__imprimirEstado(pipo, nico, juan)
        
        print("\nCocinando pedidos...")
        pipo.cocinar()

        self.__imprimirEstado(pipo, nico, juan)

        nico.tomarPizzas(pipo.entregar(orden1))
        juan.tomarPizzas(pipo.entregar(orden2))
        
        self.__imprimirEstado(pipo, nico, juan)

        print("")
        nico.servirPizzas()
        juan.servirPizzas()
        
        self.__imprimirEstado(pipo, nico, juan)

        nico.tomarPizzas(pipo.entregar(orden3))
        juan.tomarPizzas(pipo.entregar(orden4))
        
        self.__imprimirEstado(pipo, nico, juan)

        print("")
        nico.servirPizzas()
        juan.servirPizzas()
        
        self.__imprimirEstado(pipo, nico, juan)

        nico.tomarPizzas(pipo.entregar(orden3))
        
        self.__imprimirEstado(pipo, nico, juan)

        print("")
        nico.servirPizzas()
        
        self.__imprimirEstado(pipo, nico, juan)

    def __imprimirEstado(self, maestroPizzero: MaestroPizzero, mozo1: Mozo, mozo2: Mozo):
        print("\nMaestro Pizzero: " + maestroPizzero.obtenerNombre() + "\n==============================")
        print(maestroPizzero.obtenerOrdenes())
        print("==============================\nMozo: " + mozo1.obtenerNombre() + "\n==============================")
        print(mozo1.obtenerPizzas())
        print("==============================\nMozo: " + mozo2.obtenerNombre() + "\n==============================")
        print(mozo2.obtenerPizzas())

if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
