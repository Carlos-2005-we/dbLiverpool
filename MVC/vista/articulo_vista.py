from tkinter import Tk, Label, Entry, Button
from controlador.articulo_controlador import ArticuloControlador

class ArticuloVista:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x600")
        self.ventana.title("Registro de Artículos")

        Label(self.ventana, text="Artículo", bg="blue", fg="white", font=("Arial", 14)).pack(fill="x", pady=10)

        self.ingreso_idArticulo = self._crear_entrada("ID del Artículo")
        self.ingreso_Nombre = self._crear_entrada("Nombre")
        self.ingreso_Precio = self._crear_entrada("Precio")
        self.ingreso_Stock = self._crear_entrada("Stock")
        self.ingreso_Categoria = self._crear_entrada("Categoría (ID)")
        self.ingreso_Almacen = self._crear_entrada("Almacén (ID)")

        self.controlador = ArticuloControlador(self)

        Button(self.ventana, text="Registrar Artículo", bg="green", fg="white", command=self.controlador.insertar).pack(pady=5)
        Button(self.ventana, text="Ver Artículos", bg="blue", fg="white", command=self.controlador.ver_todos).pack(pady=5)
        Button(self.ventana, text="Editar Artículo", bg="orange", fg="white", command=self.controlador.actualizar).pack(pady=5)
        Button(self.ventana, text="Eliminar Artículo", bg="red", fg="white", command=self.controlador.eliminar).pack(pady=5)

        self.ventana.mainloop()

    def _crear_entrada(self, texto):
        Label(self.ventana, text=texto, bg="pink").pack(fill="x")
        entrada = Entry(self.ventana)
        entrada.pack(fill="x")
        return entrada

    def obtener_datos(self):
        return (
            self.ingreso_idArticulo.get(),
            self.ingreso_Nombre.get(),
            self.ingreso_Precio.get(),
            self.ingreso_Stock.get(),
            self.ingreso_Categoria.get(),
            self.ingreso_Almacen.get()
        )

    def limpiar_campos(self):
        for entrada in [
            self.ingreso_idArticulo, self.ingreso_Nombre, self.ingreso_Precio,
            self.ingreso_Stock, self.ingreso_Categoria, self.ingreso_Almacen
        ]:
            entrada.delete(0, 'end')
