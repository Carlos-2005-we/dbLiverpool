# controlador/cliente_controlador.py
from modelo.cliente_modelo import ClienteModelo

class ClienteController:
    def __init__(self, vista):
        self.modelo = ClienteModelo()
        self.vista = vista  # Se pasa desde fuera (evita la importación circular)

    def insertar(self):
        try:
            datos = self.vista.obtener_datos()
            self.modelo.insertar_cliente(datos)
            self.vista.mostrar_mensaje("Éxito", "Cliente registrado correctamente.")
            self.vista.limpiar_campos()
        except Exception as e:
            self.vista.mostrar_error(str(e))

    def ver(self):
        try:
            clientes = self.modelo.obtener_clientes()
            if clientes:
                mensaje = "\n".join([f"{c[0]} - {c[1]} {c[2]} | {c[3]} | {c[4]} | {c[5]} | {c[6]}" for c in clientes])
                self.vista.mostrar_mensaje("Clientes Registrados", mensaje)
            else:
                self.vista.mostrar_mensaje("Clientes Registrados", "No hay clientes registrados.")
        except Exception as e:
            self.vista.mostrar_error(str(e))

    def editar(self):
        id_cl = self.vista.preguntar_id("Editar Cliente", "Ingrese el ID del cliente a editar:")
        if not id_cl:
            return
        nuevo_tel = self.vista.preguntar_telefono()
        if not nuevo_tel:
            return
        try:
            filas = self.modelo.editar_cliente(id_cl, nuevo_tel)
            if filas > 0:
                self.vista.mostrar_mensaje("Éxito", "Cliente actualizado correctamente.")
            else:
                self.vista.mostrar_mensaje("Atención", "No se encontró el ID del cliente.")
        except Exception as e:
            self.vista.mostrar_error(str(e))

    def eliminar(self):
        id_cl = self.vista.preguntar_id("Eliminar Cliente", "Ingrese el ID del cliente a eliminar:")
        if not id_cl:
            return
        try:
            filas = self.modelo.eliminar_cliente(id_cl)
            if filas > 0:
                self.vista.mostrar_mensaje("Éxito", "Cliente eliminado correctamente.")
            else:
                self.vista.mostrar_mensaje("Atención", "No se encontró el ID del cliente.")
        except Exception as e:
            self.vista.mostrar_error(str(e))
