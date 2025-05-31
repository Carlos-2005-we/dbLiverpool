from tkinter import Tk, Label, Entry, Button, messagebox, Listbox, Scrollbar, END
import mysql.connector

# Función para conectar con la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Carloscenm1987.",
        database="dbliverpool"
    )

# Insertar categoría
def insertar_categoria():
    id_cat = ingreso_idCategoria.get()
    nombre = ingreso_Nombre.get()

    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO categoria (ID_Categoria, Nombre) VALUES (%s, %s)"
        cursor.execute(query, (id_cat, nombre))
        conexion.commit()
        messagebox.showinfo("Éxito", "Categoría registrada correctamente.")
        limpiar_campos()
        mostrar_categorias()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar la categoría:\n{err}")
    finally:
        conexion.close()

# Mostrar categorías
def mostrar_categorias():
    lista_categorias.delete(0, END)
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM categoria")
        for row in cursor.fetchall():
            lista_categorias.insert(END, f"{row[0]} - {row[1]}")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo mostrar:\n{err}")
    finally:
        conexion.close()

# Eliminar categoría
def eliminar_categoria():
    seleccion = lista_categorias.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Selecciona una categoría para eliminar.")
        return
    categoria = lista_categorias.get(seleccion)
    id_categoria = categoria.split(" - ")[0]

    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM categoria WHERE ID_Categoria = %s", (id_categoria,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Categoría eliminada correctamente.")
        mostrar_categorias()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo eliminar:\n{err}")
    finally:
        conexion.close()

# Editar categoría
def editar_categoria():
    id_cat = ingreso_idCategoria.get()
    nombre = ingreso_Nombre.get()

    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("UPDATE categoria SET Nombre = %s WHERE ID_Categoria = %s", (nombre, id_cat))
        conexion.commit()
        messagebox.showinfo("Éxito", "Categoría actualizada correctamente.")
        limpiar_campos()
        mostrar_categorias()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo actualizar:\n{err}")
    finally:
        conexion.close()

# Cargar datos seleccionados
def cargar_datos(event):
    seleccion = lista_categorias.curselection()
    if seleccion:
        categoria = lista_categorias.get(seleccion)
        id_categoria, nombre = categoria.split(" - ")
        ingreso_idCategoria.delete(0, END)
        ingreso_idCategoria.insert(0, id_categoria)
        ingreso_Nombre.delete(0, END)
        ingreso_Nombre.insert(0, nombre)

# Limpiar entradas
def limpiar_campos():
    ingreso_idCategoria.delete(0, END)
    ingreso_Nombre.delete(0, END)

# Interfaz gráfica
ventana = Tk()
ventana.geometry("400x500")
ventana.title("Gestión de Categorías")

Label(ventana, text="Gestión de Categorías", bg="blue", fg="white", font=("Arial", 14)).pack(fill="x", pady=10)

Label(ventana, text="ID Categoría", bg="pink").pack(fill="x")
ingreso_idCategoria = Entry(ventana)
ingreso_idCategoria.pack(fill="x")

Label(ventana, text="Nombre de la Categoría", bg="pink").pack(fill="x")
ingreso_Nombre = Entry(ventana)
ingreso_Nombre.pack(fill="x")

Button(ventana, text="Registrar", bg="green", fg="white", command=insertar_categoria).pack(pady=5)
Button(ventana, text="Editar", bg="orange", fg="white", command=editar_categoria).pack(pady=5)
Button(ventana, text="Eliminar", bg="red", fg="white", command=eliminar_categoria).pack(pady=5)
Button(ventana, text="Mostrar Categorías", command=mostrar_categorias).pack(pady=5)

Label(ventana, text="Lista de Categorías", bg="lightblue").pack(fill="x", pady=5)

scroll = Scrollbar(ventana)
scroll.pack(side="right", fill="y")

lista_categorias = Listbox(ventana, yscrollcommand=scroll.set)
lista_categorias.pack(fill="both", expand=True)
lista_categorias.bind("<<ListboxSelect>>", cargar_datos)
scroll.config(command=lista_categorias.yview)

mostrar_categorias()

ventana.mainloop()
