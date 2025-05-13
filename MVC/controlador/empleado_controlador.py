from modelo.empleado_modelo import EmpleadoModelo
from tkinter import messagebox, simpledialog

class EmpleadoControlador:
    def __init__(self, vista):
        self.modelo = EmpleadoModelo()
        self.vista = vista

    def registrar_empleado(self):
        datos = self.vista.obtener_datos_entrada()
        try:
            self.modelo.insertar(datos)
            messagebox.showinfo("Éxito", "Empleado registrado correctamente.")
            self.vista.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar: {e}")

    def mostrar_empleados(self):
        try:
            empleados = self.modelo.obtener_todos()
            if empleados:
                mensaje = "\n".join([f"{e[0]} - {e[1]} {e[2]} | {e[3]} | {e[4]} | ${e[5]}" for e in empleados])
                messagebox.showinfo("Empleados", mensaje)
            else:
                messagebox.showinfo("Empleados", "No hay empleados registrados.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener empleados: {e}")

    def editar_empleado(self):
        id_emp = simpledialog.askstring("Editar", "ID del empleado:")
        if not id_emp:
            return
        nuevo_salario = simpledialog.askfloat("Salario", f"Nuevo salario para {id_emp}:")
        if nuevo_salario is None:
            return
        try:
            filas = self.modelo.actualizar_salario(id_emp, nuevo_salario)
            if filas > 0:
                messagebox.showinfo("Éxito", "Salario actualizado.")
            else:
                messagebox.showwarning("Atención", "ID no encontrado.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo editar: {e}")

    def eliminar_empleado(self):
        id_emp = simpledialog.askstring("Eliminar", "ID del empleado:")
        if not id_emp:
            return
        try:
            filas = self.modelo.eliminar(id_emp)
            if filas > 0:
                messagebox.showinfo("Éxito", "Empleado eliminado.")
            else:
                messagebox.showwarning("Atención", "ID no encontrado.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar: {e}")
