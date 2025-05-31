from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, Text
import mysql.connector

# Función para insertar en la tabla almacen
def insertar_almacen():
    existencia = ingreso_existencia.get()
    articulo_proveedor = ingreso_articulo.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            INSERT INTO almacen (Existencia, Articulos_proveedor)
            VALUES (%s, %s)
        """
        cursor.execute(query, (existencia, articulo_proveedor))
        conexion.commit()
        messagebox.showinfo("Éxito", "Almacén registrado correctamente.")
        limpiar_campos()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar el almacén:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función para ver registros
def ver_almacenes():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM almacen")
        resultados = cursor.fetchall()

        ventana_ver = Toplevel()
        ventana_ver.title("Almacenes Registrados")
        texto = Text(ventana_ver, width=80, height=20)
        texto.pack()

        for fila in resultados:
            texto.insert("end", f"{fila}\n")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo obtener los almacenes:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función para editar registro
def editar_almacen():
    no_lote = ingreso_lote.get()
    existencia = ingreso_existencia.get()
    articulo_proveedor = ingreso_articulo.get()

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        query = """
            UPDATE almacen
            SET Existencia = %s, Articulos_proveedor = %s
            WHERE No_Lote_Almacen = %s
        """
        cursor.execute(query, (existencia, articulo_proveedor, no_lote))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Almacén actualizado correctamente.")
        else:
            messagebox.showwarning("Atención", "No se encontró el almacén con ese número de lote.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo actualizar el almacén:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función para eliminar
def eliminar_almacen():
    no_lote = ingreso_lote.get()
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )
        cursor = conexion.cursor()
        # Verifica si hay artículos asociados a este almacén
        cursor.execute("SELECT COUNT(*) FROM articulo WHERE almacen = %s", (no_lote,))
        asociados = cursor.fetchone()[0]
        if asociados > 0:
            messagebox.showwarning("No permitido", "No se puede eliminar el almacén porque hay artículos asociados a él.")
            return
        query = "DELETE FROM almacen WHERE No_Lote_Almacen = %s"
        cursor.execute(query, (no_lote,))
        conexion.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Almacén eliminado correctamente.")
            limpiar_campos()
        else:
            messagebox.showwarning("Atención", "No se encontró el almacén con ese número de lote.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar el almacén:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Limpiar campos
def limpiar_campos():
    ingreso_lote.delete(0, 'end')
    ingreso_existencia.delete(0, 'end')
    ingreso_articulo.delete(0, 'end')

# Interfaz
ventana = Tk()
ventana.geometry("400x500")
ventana.title("Registro de Almacenes")

Label(ventana, text="Almacén", bg="blue", fg="white", font=("Arial", 14)).pack(side="top", fill="x", pady=10)

Label(ventana, text="Número de Lote del Almacén", bg="lightgray").pack(fill="x")
ingreso_lote = Entry(ventana)
ingreso_lote.pack(fill="x")

Label(ventana, text="Existencia", bg="lightgray").pack(fill="x")
ingreso_existencia = Entry(ventana)
ingreso_existencia.pack(fill="x")

Label(ventana, text="Artículo del Proveedor", bg="lightgray").pack(fill="x")
ingreso_articulo = Entry(ventana)
ingreso_articulo.pack(fill="x")

Button(ventana, text="Registrar Almacén", bg="green", fg="white", command=insertar_almacen).pack(pady=5)
Button(ventana, text="Ver Almacenes", bg="blue", fg="white", command=ver_almacenes).pack(pady=5)
Button(ventana, text="Editar Almacén", bg="orange", fg="white", command=editar_almacen).pack(pady=5)
Button(ventana, text="Eliminar Almacén", bg="red", fg="white", command=eliminar_almacen).pack(pady=5)

ventana.mainloop()
