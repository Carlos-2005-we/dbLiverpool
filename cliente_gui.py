from tkinter import Tk, Label, Entry, Button, messagebox, simpledialog
import mysql.connector

def insertar_cliente():
    id_cliente = ingreso_idCliente.get()
    nombre = ingreso_Nombre.get()
    apellido = ingreso_Apellido.get()
    direccion = ingreso_Direccion.get()
    telefono = ingreso_Telefono.get()
    correo = ingreso_Correo.get()
    rfc = ingreso_RFC.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            INSERT INTO cliente (ID_Cliente, Nombre, Apellido, Direccion, Telefono, Correo_Electronico, RFC)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (id_cliente, nombre, apellido, direccion, telefono, correo, rfc)
        cursor.execute(query, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
        limpiar_campos()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar el cliente:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def ver_clientes():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        mensaje = "\n".join([f"{c[0]} - {c[1]} {c[2]} | {c[3]} | {c[4]} | {c[5]} | {c[6]}" for c in clientes])
        if clientes:
            messagebox.showinfo("Clientes Registrados", mensaje)
        else:
            messagebox.showinfo("Clientes Registrados", "No hay clientes registrados.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo obtener la información:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def editar_cliente():
    id_cl = simpledialog.askstring("Editar Cliente", "Ingrese el ID del cliente a editar:")
    if not id_cl:
        return

    nuevo_telefono = simpledialog.askstring("Nuevo Teléfono", f"Ingrese el nuevo teléfono para {id_cl}:")
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
        query = "UPDATE cliente SET Telefono = %s WHERE ID_Cliente = %s"
        cursor.execute(query, (nuevo_telefono, id_cl))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el ID del cliente.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo editar el cliente:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminar_cliente():
    id_cl = simpledialog.askstring("Eliminar Cliente", "Ingrese el ID del cliente a eliminar:")
    if not id_cl:
        return

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = "DELETE FROM cliente WHERE ID_Cliente = %s"
        cursor.execute(query, (id_cl,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el ID del cliente.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar el cliente:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def limpiar_campos():
    ingreso_idCliente.delete(0, 'end')
    ingreso_Nombre.delete(0, 'end')
    ingreso_Apellido.delete(0, 'end')
    ingreso_Direccion.delete(0, 'end')
    ingreso_Telefono.delete(0, 'end')
    ingreso_Correo.delete(0, 'end')
    ingreso_RFC.delete(0, 'end')

# Interfaz
ventana = Tk()
ventana.geometry("420x600")
ventana.title("Registro de Clientes")

Label(ventana, text="Cliente", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

Label(ventana, text="ID del Cliente", bg="pink").pack(fill="x")
ingreso_idCliente = Entry(ventana)
ingreso_idCliente.pack(fill="x")

Label(ventana, text="Nombre", bg="pink").pack(fill="x")
ingreso_Nombre = Entry(ventana)
ingreso_Nombre.pack(fill="x")

Label(ventana, text="Apellido", bg="pink").pack(fill="x")
ingreso_Apellido = Entry(ventana)
ingreso_Apellido.pack(fill="x")

Label(ventana, text="Dirección", bg="pink").pack(fill="x")
ingreso_Direccion = Entry(ventana)
ingreso_Direccion.pack(fill="x")

Label(ventana, text="Teléfono", bg="pink").pack(fill="x")
ingreso_Telefono = Entry(ventana)
ingreso_Telefono.pack(fill="x")

Label(ventana, text="Correo Electrónico", bg="pink").pack(fill="x")
ingreso_Correo = Entry(ventana)
ingreso_Correo.pack(fill="x")

Label(ventana, text="RFC", bg="pink").pack(fill="x")
ingreso_RFC = Entry(ventana)
ingreso_RFC.pack(fill="x")

Button(ventana, text="Registrar Cliente", bg="green", fg="white", command=insertar_cliente).pack(pady=10)
Button(ventana, text="Ver Clientes", bg="blue", fg="white", command=ver_clientes).pack(pady=5)
Button(ventana, text="Editar Cliente", bg="orange", fg="white", command=editar_cliente).pack(pady=5)
Button(ventana, text="Eliminar Cliente", bg="red", fg="white", command=eliminar_cliente).pack(pady=5)

ventana.mainloop()
