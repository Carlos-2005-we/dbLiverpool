import mysql.connector

class ProveedorModelo:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "Carloscenm1987.",
            "database": "dbliverpool"
        }

    def insertar(self, proveedor):
        conexion = mysql.connector.connect(**self.config)
        cursor = conexion.cursor()
        query = "INSERT INTO proveedor (ID_Proveedor, Nombre, Contacto, Telefono, Direccion) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, proveedor)
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_todos(self):
        conexion = mysql.connector.connect(**self.config)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedor")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados

    def actualizar_telefono(self, id_prov, nuevo_telefono):
        conexion = mysql.connector.connect(**self.config)
        cursor = conexion.cursor()
        cursor.execute("UPDATE proveedor SET Telefono = %s WHERE ID_Proveedor = %s", (nuevo_telefono, id_prov))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas_afectadas

    def eliminar(self, id_prov):
        conexion = mysql.connector.connect(**self.config)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM proveedor WHERE ID_Proveedor = %s", (id_prov,))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas_afectadas
