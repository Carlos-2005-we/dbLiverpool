from tkinter import Toplevel, Label, Entry, Button, messagebox
import tkinter.simpledialog as simpledialog
from controlador.cliente_controlador import ClienteController

class ClienteVista:
    def __init__(self):
        self.ventana = Toplevel()
        self.ventana.title("Gestión de Clientes")
        self.ventana.geometry("420x600")

        Label(self.ventana, text="Cliente", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

        self.campos = {}
        for campo in ["ID del Cliente", "Nombre", "Apellido", "Dirección", "Teléfono", "Correo Electrónico", "RFC"]:
            Label(self.ventana, text=campo, bg="pink").pack(fill="x")
            entrada = Entry(self.ventana)
            entrada.pack(fill="x")
            self.campos[campo] = entrada

        self.controlador = ClienteController(self)

        Button(self.ventana, text="Registrar Cliente", bg="green", fg="white", command=self.controlador.insertar).pack(pady=10)
        Button(self.ventana, text="Ver Clientes", bg="blue", fg="white", command=self.controlador.ver).pack(pady=5)
        Button(self.ventana, text="Editar Cliente", bg="orange", fg="white", command=self.controlador.editar).pack(pady=5)
        Button(self.ventana, text="Eliminar Cliente", bg="red", fg="white", command=self.controlador.eliminar).pack(pady=5)

    def obtener_datos(self):
        return tuple(entrada.get() for entrada in self.campos.values())

    def limpiar_campos(self):
        for entrada in self.campos.values():
            entrada.delete(0, 'end')

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def preguntar_id(self, titulo="ID", mensaje="Ingrese el ID:"):
        return simpledialog.askstring(titulo, mensaje)

    def preguntar_telefono(self, titulo="Teléfono", mensaje="Ingrese el nuevo teléfono:"):
        return simpledialog.askstring(titulo, mensaje)
