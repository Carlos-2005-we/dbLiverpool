from tkinter import Toplevel, Label, Entry, Button
from controlador.proveedor_controlador import ProveedorControlador

class ProveedorVista:
    def __init__(self):
        self.ventana = Toplevel()
        self.ventana.geometry("400x600")
        self.ventana.title("Registro de Proveedores")
        self.controlador = ProveedorControlador(self)
        self.crear_interfaz()

    def crear_interfaz(self):
        Label(self.ventana, text="Proveedor", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

        Label(self.ventana, text="ID del Proveedor", bg="pink").pack(fill="x")
        self.ingreso_idProveedor = Entry(self.ventana)
        self.ingreso_idProveedor.pack(fill="x")

        Label(self.ventana, text="Nombre", bg="pink").pack(fill="x")
        self.ingreso_Nombre = Entry(self.ventana)
        self.ingreso_Nombre.pack(fill="x")

        Label(self.ventana, text="Contacto", bg="pink").pack(fill="x")
        self.ingreso_Contacto = Entry(self.ventana)
        self.ingreso_Contacto.pack(fill="x")

        Label(self.ventana, text="Teléfono", bg="pink").pack(fill="x")
        self.ingreso_Telefono = Entry(self.ventana)
        self.ingreso_Telefono.pack(fill="x")

        Label(self.ventana, text="Dirección", bg="pink").pack(fill="x")
        self.ingreso_Direccion = Entry(self.ventana)
        self.ingreso_Direccion.pack(fill="x")

        Button(self.ventana, text="Registrar Proveedor", bg="green", fg="white", command=self.controlador.insertar_proveedor).pack(pady=10)
        Button(self.ventana, text="Ver Proveedores", bg="blue", fg="white", command=self.controlador.ver_proveedores).pack(pady=5)
        Button(self.ventana, text="Editar Proveedor", bg="orange", fg="white", command=self.controlador.editar_proveedor).pack(pady=5)
        Button(self.ventana, text="Eliminar Proveedor", bg="red", fg="white", command=self.controlador.eliminar_proveedor).pack(pady=5)

    def obtener_datos_entrada(self):
        return (
            self.ingreso_idProveedor.get(),
            self.ingreso_Nombre.get(),
            self.ingreso_Contacto.get(),
            self.ingreso_Telefono.get(),
            self.ingreso_Direccion.get()
        )

    def limpiar_campos(self):
        self.ingreso_idProveedor.delete(0, 'end')
        self.ingreso_Nombre.delete(0, 'end')
        self.ingreso_Contacto.delete(0, 'end')
        self.ingreso_Telefono.delete(0, 'end')
        self.ingreso_Direccion.delete(0, 'end')
