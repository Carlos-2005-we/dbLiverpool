from tkinter import messagebox, Toplevel, Text
from modelo.articulo_modelo import ArticuloModelo

class ArticuloControlador:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ArticuloModelo()

    def insertar(self):
        datos = self.vista.obtener_datos()
        try:
            self.modelo.insertar(*datos)
            messagebox.showinfo("Éxito", "Artículo registrado correctamente.")
            self.vista.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el artículo:\n{e}")

    def ver_todos(self):
        try:
            articulos = self.modelo.obtener_todos()
            ventana = Toplevel()
            ventana.title("Artículos Registrados")
            texto = Text(ventana, width=80, height=20)
            texto.pack()
            for art in articulos:
                texto.insert("end", f"{art}\n")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron obtener los artículos:\n{e}")

    def actualizar(self):
        datos = self.vista.obtener_datos()
        try:
            actualizado = self.modelo.actualizar(*datos)
            if actualizado:
                messagebox.showinfo("Éxito", "Artículo actualizado correctamente.")
            else:
                messagebox.showwarning("Atención", "No se encontró el artículo con ese ID.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el artículo:\n{e}")

    def eliminar(self):
        id_articulo = self.vista.ingreso_idArticulo.get()
        try:
            eliminado = self.modelo.eliminar(id_articulo)
            if eliminado:
                messagebox.showinfo("Éxito", "Artículo eliminado correctamente.")
                self.vista.limpiar_campos()
            else:
                messagebox.showwarning("Atención", "No se encontró el artículo con ese ID.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el artículo:\n{e}")
