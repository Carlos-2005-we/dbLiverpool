import mysql.connector

class ArticuloModelo:
    def __init__(self):
        self.config_db = {
            "host": "localhost",
            "user": "root",
            "password": "Carloscenm1987.",
            "database": "dbliverpool"
        }

    def conectar(self):
        return mysql.connector.connect(**self.config_db)

    def insertar(self, id_articulo, nombre, precio, stock, categoria, almacen):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = """
            INSERT INTO articulo (ID_Articulo, Nombre, Precio, Existencia, categoria, almacen)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (id_articulo, nombre, precio, stock, categoria, almacen))
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_todos(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM articulo")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultados

    def actualizar(self, id_articulo, nombre, precio, stock, categoria, almacen):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = """
            UPDATE articulo
            SET Nombre = %s, Precio = %s, Existencia = %s, categoria = %s, almacen = %s
            WHERE ID_Articulo = %s
        """
        cursor.execute(query, (nombre, precio, stock, categoria, almacen, id_articulo))
        conexion.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conexion.close()
        return rowcount

    def eliminar(self, id_articulo):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM articulo WHERE ID_Articulo = %s", (id_articulo,))
        conexion.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conexion.close()
        return rowcount
