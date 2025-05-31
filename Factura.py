from tkinter import Frame, StringVar, Tk, Label, Entry, Button, messagebox, Listbox, END, Scrollbar, SINGLE, Toplevel, OptionMenu
import mysql.connector
from datetime import datetime
from random import randint

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Carloscenm1987.",
        database="dbliverpool"
    )

carrito = []
cliente_actual = None

def generar_id_venta():
    # V + yymmdd + 3 dígitos aleatorios = 10 caracteres
    return "V" + datetime.now().strftime("%y%m%d") + str(randint(100, 999))

def buscar_cliente():
    global cliente_actual
    id_cliente = ingreso_idCliente.get()
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente WHERE ID_Cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()
        if cliente:
            cliente_actual = cliente
            lbl_datos_cliente.config(text=f"Nombre: {cliente[1]} {cliente[2]}\nTel: {cliente[4]}\nCorreo: {cliente[5]}")
        else:
            cliente_actual = ("0000", "Cliente", "General", "", "", "", "")
            lbl_datos_cliente.config(text="Cliente general")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo buscar el cliente:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def agregar_articulo():
    id_articulo = ingreso_idArticulo.get()
    cantidad = ingreso_cantidad.get()
    if not id_articulo or not cantidad:
        messagebox.showwarning("Faltan datos", "Ingrese el código y la cantidad.")
        return
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Cantidad inválida", "La cantidad debe ser un número positivo.")
        return
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT ID_Articulo, Nombre, Precio, Existencia FROM articulo WHERE ID_Articulo = %s", (id_articulo,))
        articulo = cursor.fetchone()
        if articulo:
            if cantidad > articulo[3]:
                messagebox.showwarning("Stock insuficiente", f"Solo hay {articulo[3]} en existencia.")
                return
            # Buscar si ya está en el carrito
            for i, item in enumerate(carrito):
                if item[0] == id_articulo:
                    nueva_cantidad = item[2] + cantidad
                    if nueva_cantidad > articulo[3]:
                        messagebox.showwarning("Stock insuficiente", f"Solo hay {articulo[3]} en existencia.")
                        return
                    carrito[i] = (item[0], item[1], nueva_cantidad, item[3], nueva_cantidad * item[3])
                    actualizar_lista_carrito()
                    return
            importe = cantidad * articulo[2]
            carrito.append((articulo[0], articulo[1], cantidad, articulo[2], importe))
            actualizar_lista_carrito()
        else:
            messagebox.showwarning("No encontrado", "No existe un artículo con ese código.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo buscar el artículo:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def actualizar_lista_carrito():
    lista_carrito.delete(0, END)
    for idx, item in enumerate(carrito):
        lista_carrito.insert(END, f"{item[0]} | {item[1]} | Cant: {item[2]} | ${item[3]:.2f} c/u | Importe: ${item[4]:.2f}")
    actualizar_total()

def eliminar_articulo():
    seleccion = lista_carrito.curselection()
    if not seleccion:
        return
    idx = seleccion[0]
    del carrito[idx]
    actualizar_lista_carrito()

def actualizar_total():
    subtotal = sum(item[4] for item in carrito)
    iva = subtotal * 0.16
    total = subtotal + iva
    lbl_total.config(text=f"Total (IVA incluido): ${total:.2f}")

def pagar():
    if not carrito:
        messagebox.showwarning("Carrito vacío", "Agregue artículos antes de pagar.")
        return
    global cliente_actual
    if not cliente_actual:
        buscar_cliente()
    id_empleado = ingreso_idEmpleado.get()
    metodo_pago = metodo_pago_var.get()
    cantidad_pagada = None
    cambio = None
    subtotal = sum(item[4] for item in carrito)
    iva = subtotal * 0.16
    total = subtotal + iva
    if not id_empleado:
        messagebox.showwarning("Faltan datos", "Ingrese el ID del empleado.")
        return
    if not metodo_pago:
        messagebox.showwarning("Faltan datos", "Seleccione el método de pago.")
        return
    if metodo_pago == "Efectivo":
        if not ingreso_cantidad_pagada or not ingreso_cantidad_pagada.get():
            messagebox.showwarning("Faltan datos", "Ingrese la cantidad pagada por el cliente.")
            return
        try:
            cantidad_pagada = float(ingreso_cantidad_pagada.get())
        except ValueError:
            messagebox.showwarning("Cantidad inválida", "La cantidad pagada debe ser un número.")
            return
        if cantidad_pagada < total:
            messagebox.showwarning("Pago insuficiente", "La cantidad pagada es menor al total.")
            return
        cambio = cantidad_pagada - total
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        # Generar un idFactura único
        id_factura = randint(100000, 999999)
        cursor.execute("SELECT 1 FROM Factura WHERE idFactura = %s", (id_factura,))
        while cursor.fetchone():
            id_factura = randint(100000, 999999)
            cursor.execute("SELECT 1 FROM Factura WHERE idFactura = %s", (id_factura,))
        # Crear factura (agrega campos para efectivo)
        cursor.execute(
            "INSERT INTO Factura (idFactura, Nombre_Establecimiento, Importe, Direc_Establecimiento, Fecha, Metodo_Pago, Cantidad_Pagada, Cambio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (id_factura, "DBLiverpool", total, "Dirección ejemplo", datetime.now().date(), metodo_pago, cantidad_pagada, cambio)
        )
        # Generar ID de venta
        id_venta = generar_id_venta()
        # Insertar venta
        cursor.execute(
            "INSERT INTO ventas (ID_Venta, Monto_Total, empleado, cliente, Factura) VALUES (%s, %s, %s, %s, %s)",
            (id_venta, total, id_empleado, cliente_actual[0], id_factura)
        )
        # Insertar detalle de venta y actualizar stock
        for item in carrito:
            cursor.execute(
                "INSERT INTO detalle_venta (Cantidad, Subtotal, venta, articulo) VALUES (%s, %s, %s, %s)",
                (item[2], item[4], id_venta, item[0])
            )
            cursor.execute(
                "UPDATE articulo SET Existencia = Existencia - %s WHERE ID_Articulo = %s",
                (item[2], item[0])
            )
        conexion.commit()
        messagebox.showinfo("Venta realizada", f"Venta registrada con éxito. Folio: {id_venta}")
        carrito.clear()
        actualizar_lista_carrito()
        if ingreso_cantidad_pagada:
            ingreso_cantidad_pagada.delete(0, END)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo registrar la venta:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

def ver_historial_ventas():
    ventana_historial = Toplevel(ventana)
    ventana_historial.title("Historial de Ventas")
    ventana_historial.geometry("600x400")

    lista_ventas = Listbox(ventana_historial, selectmode=SINGLE, width=80)
    lista_ventas.pack(fill="both", expand=True, padx=10, pady=10)
    btn_generar_factura = Button(ventana_historial, text="Generar Factura", state="disabled")
    btn_generar_factura.pack(pady=10)

    ventas = []
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT v.ID_Venta, v.Fecha, v.Monto_Total, v.empleado, v.cliente, v.Factura, f.Metodo_Pago
            FROM ventas v
            JOIN Factura f ON v.Factura = f.idFactura
            ORDER BY v.Fecha DESC
        """)
        ventas = cursor.fetchall()
        for venta in ventas:
            lista_ventas.insert(END, f"Venta: {venta[0]} | Fecha: {venta[1]} | Total: ${venta[2]:.2f} | Cliente: {venta[4]}")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo obtener el historial:\n{err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

    def mostrar_factura():
        seleccion = lista_ventas.curselection()
        if not seleccion:
            return
        idx = seleccion[0]
        venta = ventas[idx]
        try:
            conexion = conectar_bd()
            cursor = conexion.cursor()
            # Obtener datos de la factura
            cursor.execute("SELECT * FROM Factura WHERE idFactura = %s", (venta[5],))
            factura = cursor.fetchone()
            # Obtener detalle de venta
            cursor.execute("""
                SELECT dv.articulo, a.Nombre, dv.Cantidad, dv.Subtotal
                FROM detalle_venta dv
                JOIN articulo a ON dv.articulo = a.ID_Articulo
                WHERE dv.venta = %s
            """, (venta[0],))
            detalles = cursor.fetchall()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo obtener la factura:\n{err}")
            return
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
            subtotal = sum(det[3] for det in detalles)
            iva = subtotal * 0.16
            importe_total = subtotal + iva

        # Mostrar ventana de factura
        ventana_factura = Toplevel(ventana_historial)
        ventana_factura.title(f"Factura {factura[0]}")
        ventana_factura.geometry("500x500")
        Label(ventana_factura, text=f"Factura: {factura[0]}", font=("Arial", 14, "bold")).pack(pady=5)
        Label(ventana_factura, text=f"Establecimiento: {factura[1]}").pack()
        Label(ventana_factura, text=f"Dirección: {factura[3]}").pack()
        Label(ventana_factura, text=f"Fecha: {factura[4]}").pack()
        Label(ventana_factura, text=f"Método de Pago: {factura[5]}").pack()
        Label(ventana_factura, text=f"Subtotal: ${subtotal:.2f}").pack()
        Label(ventana_factura, text=f"IVA (16%): ${iva:.2f}").pack()
        Label(ventana_factura, text=f"Importe Total: ${importe_total:.2f}", font=("Arial", 12, "bold")).pack(pady=5)
        Label(ventana_factura, text="Detalle de artículos:", font=("Arial", 12, "underline")).pack(pady=5)
        for det in detalles:
            Label(ventana_factura, text=f"{det[0]} | {det[1]} | Cantidad: {det[2]} | Subtotal: ${det[3]:.2f}").pack(anchor="w")
        if factura[5] == "Efectivo":
            Label(ventana_factura, text=f"Cantidad Pagada: ${factura[6]:.2f}").pack()
            # El cambio ya fue calculado respecto al importe total al momento de la venta
            Label(ventana_factura, text=f"Cambio: ${factura[7]:.2f}").pack()
        Button(ventana_factura, text="Cerrar", command=ventana_factura.destroy).pack(pady=10)

    def habilitar_boton(event):
        if lista_ventas.curselection():
            btn_generar_factura.config(state="normal")
        else:
            btn_generar_factura.config(state="disabled")

    lista_ventas.bind("<<ListboxSelect>>", habilitar_boton)
    btn_generar_factura.config(command=mostrar_factura)

# --- Interfaz ---
ventana = Tk()
ventana.geometry("700x700")
ventana.title("Módulo de Ventas")

Label(ventana, text="ID Empleado:", bg="lightyellow").pack(fill="x")
ingreso_idEmpleado = Entry(ventana)
ingreso_idEmpleado.pack(fill="x")

Label(ventana, text="ID Cliente:", bg="lightblue").pack(fill="x")
ingreso_idCliente = Entry(ventana)
ingreso_idCliente.pack(fill="x")
ingreso_idCliente.insert(0, "0")
Button(ventana, text="Buscar Cliente", command=buscar_cliente).pack(pady=2)
lbl_datos_cliente = Label(ventana, text="Cliente general", bg="white", anchor="w", justify="left")
lbl_datos_cliente.pack(fill="x", pady=2)

Label(ventana, text="Código Artículo:", bg="lightgreen").pack(fill="x")
ingreso_idArticulo = Entry(ventana)
ingreso_idArticulo.pack(fill="x")
Label(ventana, text="Cantidad:", bg="lightgreen").pack(fill="x")
ingreso_cantidad = Entry(ventana)
ingreso_cantidad.pack(fill="x")
Button(ventana, text="Agregar Artículo", bg="green", fg="white", command=agregar_articulo).pack(pady=5)

# Método de pago
Label(ventana, text="Método de Pago:", bg="lightyellow").pack(fill="x")
metodo_pago_var = StringVar(value="Tarjeta")
opciones_pago = ["Tarjeta", "Efectivo"]

# Frame para ubicar el menú y la entrada juntos
frame_pago = Frame(ventana)
frame_pago.pack(fill="x")

opcion_pago_menu = OptionMenu(frame_pago, metodo_pago_var, *opciones_pago)
opcion_pago_menu.pack(fill="x")

# Etiqueta y entrada para cantidad recibida (se crean una vez)
lbl_cantidad_recibida = Label(ventana, text="Cantidad Recibida:", bg="lightyellow")
ingreso_cantidad_pagada = Entry(ventana)

def mostrar_entrada_efectivo(*args):
    if metodo_pago_var.get() == "Efectivo":
        lbl_cantidad_recibida.pack(after=frame_pago, fill="x")
        ingreso_cantidad_pagada.pack(after=lbl_cantidad_recibida, fill="x")
    else:
        lbl_cantidad_recibida.pack_forget()
        ingreso_cantidad_pagada.pack_forget()

metodo_pago_var.trace_add("write", mostrar_entrada_efectivo)
mostrar_entrada_efectivo()

Label(ventana, text="Carrito de Compra", bg="lightgray").pack(fill="x", pady=5)
scroll = Scrollbar(ventana)
scroll.pack(side="right", fill="y")
lista_carrito = Listbox(ventana, selectmode=SINGLE, yscrollcommand=scroll.set, width=80, height=10)
lista_carrito.pack(fill="both", expand=True)
scroll.config(command=lista_carrito.yview)
Button(ventana, text="Eliminar Artículo", bg="red", fg="white", command=eliminar_articulo).pack(pady=5)

lbl_total = Label(ventana, text="Total: $0.00", font=("Arial", 14), bg="yellow")
lbl_total.pack(fill="x", pady=10)

Button(ventana, text="Pagar", bg="blue", fg="white", font=("Arial", 14), command=lambda: pagar()).pack(pady=10)
Button(ventana, text="Ver Historial de Ventas", bg="gray", fg="white", command=ver_historial_ventas).pack(pady=10)

ventana.mainloop()