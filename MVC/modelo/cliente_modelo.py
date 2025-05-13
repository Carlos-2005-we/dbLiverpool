# modelo/cliente_modelo.py
import mysql.connector

class ClienteModelo:
    def __init__(self):
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "Carloscenm1987.",
            "database": "dbliverpool"
        }

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def insertar_cliente(self, cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = """
            INSERT INTO cliente (ID_Cliente, Nombre, Apellido, Direccion, Telefono, Correo_Electronico, RFC)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, cliente)
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_clientes(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        cursor.close()
        conexion.close()
        return clientes

    def editar_cliente(self, id_cliente, nuevo_telefono):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "UPDATE cliente SET Telefono = %s WHERE ID_Cliente = %s"
        cursor.execute(query, (nuevo_telefono, id_cliente))
        conexion.commit()
        actualizado = cursor.rowcount
        cursor.close()
        conexion.close()
        return actualizado

    def eliminar_cliente(self, id_cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "DELETE FROM cliente WHERE ID_Cliente = %s"
        cursor.execute(query, (id_cliente,))
        conexion.commit()
        eliminado = cursor.rowcount
        cursor.close()
        conexion.close()
        return eliminado
