from tkinter import Tk, Label, Entry, Button, messagebox, simpledialog
import mysql.connector

def insertar_proveedor():
    id_proveedor = ingreso_idProveedor.get()
    nombre = ingreso_Nombre.get()
    contacto = ingreso_Contacto.get()
    telefono = ingreso_Telefono.get()
    direccion = ingreso_Direccion.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            INSERT INTO proveedor (ID_Proveedor, Nombre, Contacto, Telefono, Direccion)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (id_proveedor, nombre, contacto, telefono, direccion)
        cursor.execute(query, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Proveedor registrado correctamente.")
        limpiar_campos()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar el proveedor:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def ver_proveedores():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedor")
        proveedores = cursor.fetchall()
        mensaje = "\n".join([f"{p[0]} - {p[1]} | {p[2]} | {p[3]} | {p[4]}" for p in proveedores])
        if proveedores:
            messagebox.showinfo("Proveedores Registrados", mensaje)
        else:
            messagebox.showinfo("Proveedores Registrados", "No hay proveedores registrados.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo obtener la información:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_proveedor():
    id_prov = simpledialog.askstring("Editar Proveedor", "Ingrese el ID del proveedor a editar:")
    if not id_prov:
        return

    nuevo_telefono = simpledialog.askstring("Nuevo Teléfono", f"Ingrese el nuevo teléfono para {id_prov}:")
    if not nuevo_telefono:
        return

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = "UPDATE proveedor SET Telefono = %s WHERE ID_Proveedor = %s"
        cursor.execute(query, (nuevo_telefono, id_prov))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el ID del proveedor.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo editar el proveedor:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_proveedor():
    id_prov = simpledialog.askstring("Eliminar Proveedor", "Ingrese el ID del proveedor a eliminar:")
    if not id_prov:
        return

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = "DELETE FROM proveedor WHERE ID_Proveedor = %s"
        cursor.execute(query, (id_prov,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el ID del proveedor.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar el proveedor:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def limpiar_campos():
    ingreso_idProveedor.delete(0, 'end')
    ingreso_Nombre.delete(0, 'end')
    ingreso_Contacto.delete(0, 'end')
    ingreso_Telefono.delete(0, 'end')
    ingreso_Direccion.delete(0, 'end')

# Interfaz
ventana = Tk()
ventana.geometry("400x600")
ventana.title("Registro de Proveedores")

Label(ventana, text="Proveedor", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

Label(ventana, text="ID del Proveedor", bg="pink").pack(fill="x")
ingreso_idProveedor = Entry(ventana)
ingreso_idProveedor.pack(fill="x")

Label(ventana, text="Nombre", bg="pink").pack(fill="x")
ingreso_Nombre = Entry(ventana)
ingreso_Nombre.pack(fill="x")

Label(ventana, text="Contacto", bg="pink").pack(fill="x")
ingreso_Contacto = Entry(ventana)
ingreso_Contacto.pack(fill="x")

Label(ventana, text="Teléfono", bg="pink").pack(fill="x")
ingreso_Telefono = Entry(ventana)
ingreso_Telefono.pack(fill="x")

Label(ventana, text="Dirección", bg="pink").pack(fill="x")
ingreso_Direccion = Entry(ventana)
ingreso_Direccion.pack(fill="x")

Button(ventana, text="Registrar Proveedor", bg="green", fg="white", command=insertar_proveedor).pack(pady=10)
Button(ventana, text="Ver Proveedores", bg="blue", fg="white", command=ver_proveedores).pack(pady=5)
Button(ventana, text="Editar Proveedor", bg="orange", fg="white", command=editar_proveedor).pack(pady=5)
Button(ventana, text="Eliminar Proveedor", bg="red", fg="white", command=eliminar_proveedor).pack(pady=5)

ventana.mainloop()
