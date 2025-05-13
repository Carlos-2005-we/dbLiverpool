from tkinter import Toplevel, Label, Entry, Button, Listbox, Scrollbar, END
from controlador.categoria_controller import CategoriaController

class CategoriaVista:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("400x500")
        self.root.title("Gestión de Categorías")

        Label(self.root, text="Gestión de Categorías", bg="blue", fg="white", font=("Arial", 14)).pack(fill="x", pady=10)

        Label(self.root, text="ID Categoría", bg="pink").pack(fill="x")
        self.entrada_id = Entry(self.root)
        self.entrada_id.pack(fill="x")

        Label(self.root, text="Nombre de la Categoría", bg="pink").pack(fill="x")
        self.entrada_nombre = Entry(self.root)
        self.entrada_nombre.pack(fill="x")

        self.controlador = CategoriaController(self)

        Button(self.root, text="Registrar", bg="green", fg="white", command=self.controlador.insertar).pack(pady=5)
        Button(self.root, text="Editar", bg="orange", fg="white", command=self.controlador.editar).pack(pady=5)
        Button(self.root, text="Eliminar", bg="red", fg="white", command=self.controlador.eliminar).pack(pady=5)
        Button(self.root, text="Mostrar Categorías", command=self.controlador.mostrar).pack(pady=5)

        Label(self.root, text="Lista de Categorías", bg="lightblue").pack(fill="x", pady=5)

        scroll = Scrollbar(self.root)
        scroll.pack(side="right", fill="y")

        self.lista = Listbox(self.root, yscrollcommand=scroll.set)
        self.lista.pack(fill="both", expand=True)
        self.lista.bind("<<ListboxSelect>>", self.cargar_datos)
        scroll.config(command=self.lista.yview)

        self.controlador.mostrar()

    def get_id(self):
        return self.entrada_id.get()

    def get_nombre(self):
        return self.entrada_nombre.get()

    def limpiar_campos(self):
        self.entrada_id.delete(0, END)
        self.entrada_nombre.delete(0, END)

    def limpiar_lista(self):
        self.lista.delete(0, END)

    def agregar_categoria_lista(self, texto):
        self.lista.insert(END, texto)

    def get_id_seleccionado(self):
        seleccion = self.lista.curselection()
        if seleccion:
            return self.lista.get(seleccion).split(" - ")[0]
        return None

    def cargar_datos(self, event):
        seleccion = self.lista.curselection()
        if seleccion:
            categoria = self.lista.get(seleccion)
            id_categoria, nombre = categoria.split(" - ")
            self.entrada_id.delete(0, END)
            self.entrada_id.insert(0, id_categoria)
            self.entrada_nombre.delete(0, END)
            self.entrada_nombre.insert(0, nombre)
