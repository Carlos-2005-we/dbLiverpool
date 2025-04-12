from tkinter import Tk, Label, Entry, Button, messagebox, simpledialog
import mysql.connector

def insertar_empleado():
    id_emp = ingreso_idEmpleado.get()
    nombre = ingreso_Nombre.get()
    apellido = ingreso_Apellido.get()
    puesto = ingreso_Puesto.get()
    departamento = ingreso_Departamento.get()
    salario = ingreso_Salario.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            INSERT INTO empleado (ID_Empleado, Nombre, Apellido, Puesto, Departamento, Salario)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (id_emp, nombre, apellido, puesto, departamento, salario)
        cursor.execute(query, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Empleado registrado correctamente.")
        limpiar_campos()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar el empleado:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def ver_empleados():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleado")
        empleados = cursor.fetchall()
        mensaje = "\n".join([f"{e[0]} - {e[1]} {e[2]} | {e[3]} | {e[4]} | ${e[5]}" for e in empleados])
        if empleados:
            messagebox.showinfo("Empleados Registrados", mensaje)
        else:
            messagebox.showinfo("Empleados Registrados", "No hay empleados registrados.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo obtener la información:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_empleado():
    id_emp = simpledialog.askstring("Editar Empleado", "Ingrese el ID del empleado a editar:")
    if not id_emp:
        return

    nuevo_salario = simpledialog.askfloat("Nuevo Salario", f"Ingrese el nuevo salario para {id_emp}:")
    if nuevo_salario is None:
        return

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = "UPDATE empleado SET Salario = %s WHERE ID_Empleado = %s"
        cursor.execute(query, (nuevo_salario, id_emp))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el ID del empleado.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo editar el empleado:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_empleado():
    id_emp = simpledialog.askstring("Eliminar Empleado", "Ingrese el ID del empleado a eliminar:")
    if not id_emp:
        return

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = "DELETE FROM empleado WHERE ID_Empleado = %s"
        cursor.execute(query, (id_emp,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el ID del empleado.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar el empleado:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def limpiar_campos():
    ingreso_idEmpleado.delete(0, 'end')
    ingreso_Nombre.delete(0, 'end')
    ingreso_Apellido.delete(0, 'end')
    ingreso_Puesto.delete(0, 'end')
    ingreso_Departamento.delete(0, 'end')
    ingreso_Salario.delete(0, 'end')

# Ventana principal
ventana = Tk()
ventana.geometry("400x600")
ventana.title("Gestión de Empleados")

Label(ventana, text="Empleado", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

Label(ventana, text="ID del Empleado", bg="pink").pack(fill="x")
ingreso_idEmpleado = Entry(ventana)
ingreso_idEmpleado.pack(fill="x")

Label(ventana, text="Nombre", bg="pink").pack(fill="x")
ingreso_Nombre = Entry(ventana)
ingreso_Nombre.pack(fill="x")

Label(ventana, text="Apellido", bg="pink").pack(fill="x")
ingreso_Apellido = Entry(ventana)
ingreso_Apellido.pack(fill="x")

Label(ventana, text="Puesto", bg="pink").pack(fill="x")
ingreso_Puesto = Entry(ventana)
ingreso_Puesto.pack(fill="x")

Label(ventana, text="Departamento", bg="pink").pack(fill="x")
ingreso_Departamento = Entry(ventana)
ingreso_Departamento.pack(fill="x")

Label(ventana, text="Salario", bg="pink").pack(fill="x")
ingreso_Salario = Entry(ventana)
ingreso_Salario.pack(fill="x")

Button(ventana, text="Registrar Empleado", bg="green", fg="white", command=insertar_empleado).pack(pady=10)
Button(ventana, text="Ver Empleados", bg="blue", fg="white", command=ver_empleados).pack(pady=5)
Button(ventana, text="Editar Empleado", bg="orange", fg="white", command=editar_empleado).pack(pady=5)
Button(ventana, text="Eliminar Empleado", bg="red", fg="white", command=eliminar_empleado).pack(pady=5)

ventana.mainloop()
