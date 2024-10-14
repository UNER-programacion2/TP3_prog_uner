from pizzavariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo
import os
import platform
import time


class TesterPizzeria:
    def main(self):
        #Creacion de objetos
        muzzarella = PizzaVariedad("Muzzarella", 500)
        napolitana = PizzaVariedad("Napolitana", 540)

        pizza1 = Pizza(muzzarella)
        pizza2 = Pizza(napolitana)

        orden1 = Orden(1, [pizza1, pizza2])

        maestro = MaestroPizzero("Nicolas")
        mozo = Mozo("Beatriz")

        #tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.
        maestro.tomarPedido(orden1)
        maestro.cocinar()
        
        #tomarPizzas y servirPizzas a los objetos de la clase Mozo.
        mozo.tomarPizzas([pizza1, pizza2])
        mozo.servirPizzas()
        
        #transición de estados
        print(f"Estado de la Orden {orden1.obtenerNroOrden()}: {orden1.obtenerEstadoOrden()}")
        estados_pizzas = [pizza.obtenerEstado() for pizza in orden1.obtenerPizzas()]
        print(f"Estado de las Pizzas en la Orden {orden1.obtenerNroOrden()}: {estados_pizzas}")

        #calcula  el total de la orden. 
        total1 = orden1.calcularTotal()
        print(f"Total de la Orden {orden1.obtenerNroOrden()}: {total1}")



###############################################################################################################################################################

# #ELECCION DEL USUARIO - MENU
# class TesterPizzeria:
#     def main(self):

#         #Creacion de objetos
#         maestroPizzero = MaestroPizzero("Nicolas")
#         mozo1 = Mozo("Beatriz")
#         mozo2 = Mozo("Carlos")

#     def menu():
#         print("-" * 60)
#         print("TRABAJO PRACTICO NUMERO 3")
#         print("-" * 60)
#         print("Bienvenidos a pizzería de Don Pipo, este es nuestro menú:""\n")
#         print("Opcion 1. Mostrar Pizzas\nOpcion 2. Ingresar el Pedido\nOpcion 3. Mostrar que mozo tomo el pedido\nOpcion 4. Mostrar Menu y numero de orden\nOpcion 5. Mostrar total a pagar\nOpcion 6. Salir")
#         print("-" * 60)


#     menu()
        


        
# #mostrar lista
# #ingresar pedido
# #mostrar que mozo tomo el pedido y todo eso
# #mostrar menu con nro de orden, total a pagar 

#     def limpiar_consola(self):
#         if platform.system() == "Windows":
#             os.system("cls")
#         else:
#             os.system("clear") 


    

if __name__ == '__main__':
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()