import mysql.connector

class CategoriaModel:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "Carloscenm1987.",
            "database": "dbliverpool"
        }

    def conectar(self):
        return mysql.connector.connect(**self.config)

    def insertar(self, id_cat, nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO categoria (ID_Categoria, Nombre) VALUES (%s, %s)", (id_cat, nombre))
        conexion.commit()
        conexion.close()

    def obtener_todas(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM categoria")
        datos = cursor.fetchall()
        conexion.close()
        return datos

    def eliminar(self, id_cat):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM categoria WHERE ID_Categoria = %s", (id_cat,))
        conexion.commit()
        conexion.close()

    def actualizar(self, id_cat, nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("UPDATE categoria SET Nombre = %s WHERE ID_Categoria = %s", (nombre, id_cat))
        conexion.commit()
        conexion.close()
