from tkinter import messagebox
from modelo.categoria_model import CategoriaModel


class CategoriaController:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = CategoriaModel()

    def insertar(self):
        id_cat = self.vista.get_id()
        nombre = self.vista.get_nombre()
        try:
            self.modelo.insertar(id_cat, nombre)
            messagebox.showinfo("Éxito", "Categoría registrada correctamente.")
            self.vista.limpiar_campos()
            self.mostrar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar(self):
        self.vista.limpiar_lista()
        try:
            categorias = self.modelo.obtener_todas()
            for cat in categorias:
                self.vista.agregar_categoria_lista(f"{cat[0]} - {cat[1]}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        id_cat = self.vista.get_id_seleccionado()
        if id_cat:
            try:
                self.modelo.eliminar(id_cat)
                messagebox.showinfo("Éxito", "Categoría eliminada correctamente.")
                self.mostrar()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def editar(self):
        id_cat = self.vista.get_id()
        nombre = self.vista.get_nombre()
        try:
            self.modelo.actualizar(id_cat, nombre)
            messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
            self.vista.limpiar_campos()
            self.mostrar()
        except Exception as e:
            messagebox.showerror("Error", str(e))
