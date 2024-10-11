from pizzavariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo

# class TesterPizzeria:
#     def main(self):
#         # Crear objetos
#         variedad_muzzarella = PizzaVariedad("Muzzarella", 500)
#         variedad_napolitana = PizzaVariedad("Napolitana", 600)
        
#         pizza1 = Pizza(variedad_muzzarella)
#         pizza2 = Pizza(variedad_napolitana)
        
#         orden1 = Orden(1, [pizza1, pizza2])
        
#         maestro = MaestroPizzero("Don Pipo")
#         mozo1 = Mozo("Juan")
#         mozo2 = Mozo("Pedro")
        
#         # Procesar pedidos
#         maestro.tomar_pedido(orden1)
#         maestro.cocinar()
#         pizzas_entregadas = maestro.entregar(orden1)
        
#         mozo1.tomar_pizzas(pizzas_entregadas)
#         mozo1.servir_pizzas()
        
#         # Mostrar estados y costos
#         print(f"Estado de la orden: {orden1.obtener_estado_orden()}")
#         print(f"Costo total de la orden: {orden1.calcular_total()}")

# if __name__ == '__main__':
#     tester_pizzeria = TesterPizzeria()
#     tester_pizzeria.main()


#############################################################################################################
class TesterPizzeria:
    def main(self):
        # Crear objetos
        variedad_muzzarella = PizzaVariedad("Muzzarella", 500)
        variedad_napolitana = PizzaVariedad("Napolitana", 600)
        
        pizza1 = Pizza(variedad_muzzarella)
        pizza2 = Pizza(variedad_napolitana)
        
        orden1 = Orden(1, [pizza1, pizza2])
        
        maestro = MaestroPizzero("Pedro")
        mozo1 = Mozo("Juan")
        mozo2 = Mozo("Pedro")
        
        # Procesar pedidos
        maestro.tomarPedido(orden1)
        maestro.cocinar()
        pizzas_entregadas = maestro.entregar(orden1)
        
        mozo1.tomar_pizzas(pizzas_entregadas)
        mozo1.servir_pizzas()

        mozo2.tomar_pizzas(pizzas_entregadas)
        mozo2.servir_pizzas()
        
        # Mostrar estados y costos
        print(f"Estado de la orden: {orden1.obtener_estado_orden()}")
        print(f"Costo total de la orden: {orden1.calcular_total()}")

if __name__ == '__main__':
    tester_pizzeria = TesterPizzeria()
    tester_pizzeria.main()
