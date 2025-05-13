from tkinter import Toplevel, Label, Entry, Button, Text
from controlador.almacen_controlador import AlmacenController

class AlmacenVista:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("400x500")
        self.root.title("Registro de Almacenes")

        Label(self.root, text="Almacén", bg="blue", fg="white", font=("Arial", 14)).pack(fill="x", pady=10)

        Label(self.root, text="Número de Lote del Almacén", bg="lightgray").pack(fill="x")
        self.ingreso_lote = Entry(self.root)
        self.ingreso_lote.pack(fill="x")

        Label(self.root, text="Existencia", bg="lightgray").pack(fill="x")
        self.ingreso_existencia = Entry(self.root)
        self.ingreso_existencia.pack(fill="x")

        Label(self.root, text="Artículo del Proveedor", bg="lightgray").pack(fill="x")
        self.ingreso_articulo = Entry(self.root)
        self.ingreso_articulo.pack(fill="x")

        self.controlador = AlmacenController(self)

        Button(self.root, text="Registrar Almacén", bg="green", fg="white", command=self.controlador.insertar).pack(pady=5)
        Button(self.root, text="Ver Almacenes", bg="blue", fg="white", command=self.controlador.ver_todos).pack(pady=5)
        Button(self.root, text="Editar Almacén", bg="orange", fg="white", command=self.controlador.editar).pack(pady=5)
        Button(self.root, text="Eliminar Almacén", bg="red", fg="white", command=self.controlador.eliminar).pack(pady=5)

    def get_lote(self):
        return self.ingreso_lote.get()

    def get_existencia(self):
        return self.ingreso_existencia.get()

    def get_articulo(self):
        return self.ingreso_articulo.get()

    def limpiar_campos(self):
        self.ingreso_lote.delete(0, 'end')
        self.ingreso_existencia.delete(0, 'end')
        self.ingreso_articulo.delete(0, 'end')

    def mostrar_resultados(self, resultados):
        ventana_ver = Toplevel(self.root)
        ventana_ver.title("Almacenes Registrados")
        texto = Text(ventana_ver, width=80, height=20)
        texto.pack()
        for fila in resultados:
            texto.insert("end", f"{fila}\n")
