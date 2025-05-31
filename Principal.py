from tkinter import Tk, Button, messagebox
import subprocess

# Funciones para abrir ventanas
def abrir_ventana_empleado():
    subprocess.Popen(["python", "empleado_gui.py"])

def abrir_ventana_cliente():
    subprocess.Popen(["python", "cliente_gui.py"])

def abrir_ventana_proveedor():
    subprocess.Popen(["python", "proveedor_gui.py"])

def abrir_ventana_articulos():
    subprocess.Popen(["python", "crud_articulos.py"])  

def abrir_ventana_categoria():
    subprocess.Popen(["python", "categoria_gui.py"]) 

def abrir_ventana_almacen():
    subprocess.Popen(["python", "almacen_gui.py"])
    
def abrir_ventana_venta():
    subprocess.Popen(["python", "Factura.py"])

# Ventana principal
ventana = Tk()
ventana.title("Sistema de Gestión - DBLiverpool")
ventana.geometry("300x400")

# Botones
Button(ventana, text="Registrar Empleado", command=abrir_ventana_empleado, bg="lightblue").pack(pady=10, fill="x")
Button(ventana, text="Registrar Cliente", command=abrir_ventana_cliente, bg="lightgreen").pack(pady=10, fill="x")
Button(ventana, text="Registrar Proveedor", command=abrir_ventana_proveedor, bg="lightyellow").pack(pady=10, fill="x")
Button(ventana, text="Registrar Artículo", command=abrir_ventana_articulos, bg="lightpink").pack(pady=10, fill="x")
Button(ventana, text="Gestionar Categorías", command=abrir_ventana_categoria, bg="lightgray").pack(pady=10, fill="x")
Button(ventana, text="Gestionar Almacenes", command=abrir_ventana_almacen, bg="lightsteelblue").pack(pady=10, fill="x")
Button(ventana, text="Realizar Venta", command=abrir_ventana_venta, bg="orange", fg="white").pack(pady=10, fill="x")

Button(ventana, text="Salir", command=ventana.quit, bg="red", fg="white").pack(pady=20)

ventana.mainloop()