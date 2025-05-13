import mysql.connector

class AlmacenModel:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "Carloscenm1987.",
            "database": "dbliverpool"
        }

    def conectar(self):
        return mysql.connector.connect(**self.config)

    def insertar(self, existencia, articulo_proveedor):
        conn = self.conectar()
        cursor = conn.cursor()
        query = "INSERT INTO almacen (Existencia, Articulos_proveedor) VALUES (%s, %s)"
        cursor.execute(query, (existencia, articulo_proveedor))
        conn.commit()
        cursor.close()
        conn.close()

    def obtener_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM almacen")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados

    def actualizar(self, no_lote, existencia, articulo_proveedor):
        conn = self.conectar()
        cursor = conn.cursor()
        query = "UPDATE almacen SET Existencia = %s, Articulos_proveedor = %s WHERE No_Lote_Almacen = %s"
        cursor.execute(query, (existencia, articulo_proveedor, no_lote))
        conn.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conn.close()
        return filas_afectadas

    def eliminar(self, no_lote):
        conn = self.conectar()
        cursor = conn.cursor()
        query = "DELETE FROM almacen WHERE No_Lote_Almacen = %s"
        cursor.execute(query, (no_lote,))
        conn.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conn.close()
        return filas_afectadas
