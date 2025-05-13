from tkinter import messagebox, Toplevel, Text
from modelo.almacen_model import AlmacenModel

class AlmacenController:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = AlmacenModel()

    def insertar(self):
        existencia = self.vista.get_existencia()
        articulo = self.vista.get_articulo()
        try:
            self.modelo.insertar(existencia, articulo)
            messagebox.showinfo("Éxito", "Almacén registrado correctamente.")
            self.vista.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ver_todos(self):
        try:
            resultados = self.modelo.obtener_todos()
            self.vista.mostrar_resultados(resultados)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def editar(self):
        no_lote = self.vista.get_lote()
        existencia = self.vista.get_existencia()
        articulo = self.vista.get_articulo()
        try:
            filas = self.modelo.actualizar(no_lote, existencia, articulo)
            if filas > 0:
                messagebox.showinfo("Éxito", "Almacén actualizado correctamente.")
            else:
                messagebox.showwarning("Atención", "No se encontró el almacén con ese número de lote.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        no_lote = self.vista.get_lote()
        try:
            filas = self.modelo.eliminar(no_lote)
            if filas > 0:
                messagebox.showinfo("Éxito", "Almacén eliminado correctamente.")
                self.vista.limpiar_campos()
            else:
                messagebox.showwarning("Atención", "No se encontró el almacén con ese número de lote.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
