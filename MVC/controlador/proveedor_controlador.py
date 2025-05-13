from tkinter import messagebox
from tkinter.simpledialog import askstring
from modelo.proveedor_modelo import ProveedorModelo

class ProveedorControlador:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ProveedorModelo()

    def insertar_proveedor(self):
        datos = self.vista.obtener_datos_entrada()
        try:
            self.modelo.insertar(datos)
            messagebox.showinfo("Éxito", "Proveedor registrado correctamente.")
            self.vista.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el proveedor:\n{e}")

    def ver_proveedores(self):
        try:
            proveedores = self.modelo.obtener_todos()
            if proveedores:
                mensaje = "\n".join([f"{p[0]} - {p[1]} | {p[2]} | {p[3]} | {p[4]}" for p in proveedores])
                messagebox.showinfo("Proveedores Registrados", mensaje)
            else:
                messagebox.showinfo("Proveedores Registrados", "No hay proveedores registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener la información:\n{e}")

    def editar_proveedor(self):
        id_prov = askstring("Editar Proveedor", "Ingrese el ID del proveedor a editar:")
        if not id_prov:
            return

        nuevo_telefono = askstring("Nuevo Teléfono", f"Ingrese el nuevo teléfono para {id_prov}:")
        if not nuevo_telefono:
            return

        try:
            filas_afectadas = self.modelo.actualizar_telefono(id_prov, nuevo_telefono)
            if filas_afectadas > 0:
                messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
            else:
                messagebox.showwarning("Atención", "No se encontró el ID del proveedor.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo editar el proveedor:\n{e}")

    def eliminar_proveedor(self):
        id_prov = askstring("Eliminar Proveedor", "Ingrese el ID del proveedor a eliminar:")
        if not id_prov:
            return

        try:
            filas_afectadas = self.modelo.eliminar(id_prov)
            if filas_afectadas > 0:
                messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
            else:
                messagebox.showwarning("Atención", "No se encontró el ID del proveedor.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el proveedor:\n{e}")
