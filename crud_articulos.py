from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, Text
import mysql.connector

# Función para insertar artículo en la base de datos
def insertar_articulo():
    id_articulo = ingreso_idArticulo.get()
    nombre = ingreso_Nombre.get()
    precio = ingreso_Precio.get()
    stock = ingreso_Stock.get()
    categoria = ingreso_Categoria.get()
    almacen = ingreso_Almacen.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            INSERT INTO articulo (ID_Articulo, Nombre, Precio, Existencia, categoria, almacen)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (id_articulo, nombre, precio, stock, categoria, almacen)
        cursor.execute(query, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Artículo registrado correctamente.")
        limpiar_campos()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar el artículo:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Ver artículos registrados
def ver_articulos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM articulo")
        resultados = cursor.fetchall()

        ventana_ver = Toplevel()
        ventana_ver.title("Artículos Registrados")
        texto = Text(ventana_ver, width=80, height=20)
        texto.pack()

        for fila in resultados:
            texto.insert("end", f"{fila}\n")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo obtener los artículos:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Editar artículo
def editar_articulo():
    id_articulo = ingreso_idArticulo.get()
    nombre = ingreso_Nombre.get()
    precio = ingreso_Precio.get()
    stock = ingreso_Stock.get()
    categoria = ingreso_Categoria.get()
    almacen = ingreso_Almacen.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            UPDATE articulo
            SET Nombre = %s, Precio = %s, Existencia = %s, categoria = %s, almacen = %s
            WHERE ID_Articulo = %s
        """
        valores = (nombre, precio, stock, categoria, almacen, id_articulo)
        cursor.execute(query, valores)
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Artículo actualizado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el artículo con ese ID.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo actualizar el artículo:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Eliminar artículo
def eliminar_articulo():
    id_articulo = ingreso_idArticulo.get()
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = "DELETE FROM articulo WHERE ID_Articulo = %s"
        cursor.execute(query, (id_articulo,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Artículo eliminado correctamente.")
            limpiar_campos()
        else:
            messagebox.showwarning("Atención", "No se encontró el artículo con ese ID.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar el artículo:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Limpiar campos
def limpiar_campos():
    ingreso_idArticulo.delete(0, 'end')
    ingreso_Nombre.delete(0, 'end')
    ingreso_Precio.delete(0, 'end')
    ingreso_Stock.delete(0, 'end')
    ingreso_Categoria.delete(0, 'end')
    ingreso_Almacen.delete(0, 'end')

# Interfaz
ventana = Tk()
ventana.geometry("400x600")
ventana.title("Registro de Artículos")

Label(ventana, text="Artículo", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

Label(ventana, text="ID del Artículo", bg="pink").pack(fill="x")
ingreso_idArticulo = Entry(ventana)
ingreso_idArticulo.pack(fill="x")

Label(ventana, text="Nombre", bg="pink").pack(fill="x")
ingreso_Nombre = Entry(ventana)
ingreso_Nombre.pack(fill="x")

Label(ventana, text="Precio", bg="pink").pack(fill="x")
ingreso_Precio = Entry(ventana)
ingreso_Precio.pack(fill="x")

Label(ventana, text="Stock", bg="pink").pack(fill="x")
ingreso_Stock = Entry(ventana)
ingreso_Stock.pack(fill="x")

Label(ventana, text="Categoría (ID)", bg="pink").pack(fill="x")
ingreso_Categoria = Entry(ventana)
ingreso_Categoria.pack(fill="x")

Label(ventana, text="Almacén (ID)", bg="pink").pack(fill="x")
ingreso_Almacen = Entry(ventana)
ingreso_Almacen.pack(fill="x")

Button(ventana, text="Registrar Artículo", bg="green", fg="white", command=insertar_articulo).pack(pady=5)
Button(ventana, text="Ver Artículos", bg="blue", fg="white", command=ver_articulos).pack(pady=5)
Button(ventana, text="Editar Artículo", bg="orange", fg="white", command=editar_articulo).pack(pady=5)
Button(ventana, text="Eliminar Artículo", bg="red", fg="white", command=eliminar_articulo).pack(pady=5)

ventana.mainloop()
