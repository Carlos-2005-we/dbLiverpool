import mysql.connector

class EmpleadoModelo:
    def conectar(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Carloscenm1987.",
            database="dbliverpool"
        )

    def insertar(self, datos):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = """
            INSERT INTO empleado (ID_Empleado, Nombre, Apellido, Puesto, Departamento, Salario)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_todos(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleado")
        resultado = cursor.fetchall()
        cursor.close()
        conexion.close()
        return resultado

    def actualizar_salario(self, id_empleado, nuevo_salario):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "UPDATE empleado SET Salario = %s WHERE ID_Empleado = %s"
        cursor.execute(query, (nuevo_salario, id_empleado))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas_afectadas

    def eliminar(self, id_empleado):
        conexion = self.conectar()
        cursor = conexion.cursor()
        query = "DELETE FROM empleado WHERE ID_Empleado = %s"
        cursor.execute(query, (id_empleado,))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return filas_afectadas
