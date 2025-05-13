from tkinter import Tk, Label, Entry, Button
from controlador.empleado_controlador import EmpleadoControlador

class EmpleadoVista:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x600")
        self.ventana.title("Gestión de Empleados")

        # Inicializar el controlador antes de los widgets
        self.controlador = EmpleadoControlador(self)
        self.crear_widgets()

        self.ventana.mainloop()

    def crear_widgets(self):
        Label(self.ventana, text="Empleado", bg="blue", fg="white", font=("Arial", 14)).pack(fill="x", pady=10)

        self.ingreso_id = self.crear_input("ID del Empleado")
        self.ingreso_nombre = self.crear_input("Nombre")
        self.ingreso_apellido = self.crear_input("Apellido")
        self.ingreso_puesto = self.crear_input("Puesto")
        self.ingreso_departamento = self.crear_input("Departamento")
        self.ingreso_salario = self.crear_input("Salario")

        Button(self.ventana, text="Registrar Empleado", bg="green", fg="white", command=self.controlador.registrar_empleado).pack(pady=10)
        Button(self.ventana, text="Ver Empleados", bg="blue", fg="white", command=self.controlador.mostrar_empleados).pack(pady=5)
        Button(self.ventana, text="Editar Empleado", bg="orange", fg="white", command=self.controlador.editar_empleado).pack(pady=5)
        Button(self.ventana, text="Eliminar Empleado", bg="red", fg="white", command=self.controlador.eliminar_empleado).pack(pady=5)

    def crear_input(self, texto):
        Label(self.ventana, text=texto, bg="pink").pack(fill="x")
        entrada = Entry(self.ventana)
        entrada.pack(fill="x")
        return entrada

    def obtener_datos_entrada(self):
        return (
            self.ingreso_id.get(),
            self.ingreso_nombre.get(),
            self.ingreso_apellido.get(),
            self.ingreso_puesto.get(),
            self.ingreso_departamento.get(),
            self.ingreso_salario.get()
        )

    def limpiar_campos(self):
        for campo in [self.ingreso_id, self.ingreso_nombre, self.ingreso_apellido,
                      self.ingreso_puesto, self.ingreso_departamento, self.ingreso_salario]:
            campo.delete(0, 'end')
