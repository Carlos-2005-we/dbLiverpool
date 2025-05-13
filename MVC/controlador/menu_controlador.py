import subprocess

class MenuControlador:
    def abrir_ventana_empleado(self):
        subprocess.Popen(["python", "empleado_gui.py"])

    def abrir_ventana_cliente(self):
        subprocess.Popen(["python", "cliente_gui.py"])

    def abrir_ventana_proveedor(self):
        subprocess.Popen(["python", "proveedor_gui.py"])

    def abrir_ventana_articulos(self):
        subprocess.Popen(["python", "crud_articulos.py"])

    def abrir_ventana_categoria(self):
        subprocess.Popen(["python", "categoria_gui.py"])

    def abrir_ventana_almacen(self):
        subprocess.Popen(["python", "almacen_gui.py"])
