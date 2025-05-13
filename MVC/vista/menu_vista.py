from tkinter import Tk, Button
from vista.empleado_vista import EmpleadoVista
from vista.cliente_vista import ClienteVista
from vista.proveedor_vista import ProveedorVista
from vista.articulo_vista import ArticuloVista
from vista.categoria_vista import CategoriaVista
from vista.almacen_vista import AlmacenVista

def abrir_ventana_empleado():
    EmpleadoVista()

def abrir_ventana_cliente():
    ClienteVista()

def abrir_ventana_proveedor():
    ProveedorVista()

def abrir_ventana_articulos():
    ArticuloVista()

def abrir_ventana_categoria():
    CategoriaVista()

def abrir_ventana_almacen():
    AlmacenVista()

# Ventana principal
ventana = Tk()
ventana.title("Sistema de Gestión - DBLiverpool")
ventana.geometry("300x400")

Button(ventana, text="Registrar Empleado", command=abrir_ventana_empleado, bg="lightblue").pack(pady=10, fill="x")
Button(ventana, text="Registrar Cliente", command=abrir_ventana_cliente, bg="lightgreen").pack(pady=10, fill="x")
Button(ventana, text="Registrar Proveedor", command=abrir_ventana_proveedor, bg="lightyellow").pack(pady=10, fill="x")
Button(ventana, text="Registrar Artículo", command=abrir_ventana_articulos, bg="lightpink").pack(pady=10, fill="x")
Button(ventana, text="Gestionar Categorías", command=abrir_ventana_categoria, bg="lightgray").pack(pady=10, fill="x")
Button(ventana, text="Gestionar Almacenes", command=abrir_ventana_almacen, bg="lightsteelblue").pack(pady=10, fill="x")

Button(ventana, text="Salir", command=ventana.quit, bg="red", fg="white").pack(pady=20)

ventana.mainloop()
