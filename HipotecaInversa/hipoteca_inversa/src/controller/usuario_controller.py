import sys
sys.path.append( "src" )

import psycopg2

from model.model.usuario import Usuario
import SecretConfig

class ControladorUsuario:
    def crear_tabla():
        cursor=ControladorUsuario.ObtenerCursor()
        cursor.execute("""CREATE TABLE usuarios (
        cedula VARCHAR(20) PRIMARY KEY,
        edad INT NOT NULL,
        expectativa_vida INT NOT NULL,
        anos_renta INT NOT NULL,
        total_cuotas INT NOT NULL,
        precio_vivienda DECIMAL(15, 2) NOT NULL,
        porcentaje_precio_real DECIMAL(5, 2) NOT NULL,  
        valor_hipoteca DECIMAL(15, 2) NOT NULL,
        ingreso_mensual DECIMAL(15, 2) NOT NULL,
        tasa_interes_mensual DECIMAL(5, 4) NOT NULL     
        );""")
        cursor.connection.commit()
    def eliminar_tabla():
        cursor = ControladorUsuario.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        cursor.connection.commit()
    def InsertarUsuario():
        cursor=ControladorUsuario.ObtenerCursor()
        cursor.execute("""INSERT INTO usuarios (
          edad,
          expectativa_vida,
          años_renta,
          total_cuotas,
          precio_de_la_vivienda,
          porcentaje_precio_real,
          valor_de_la_hipoteca,
          tasa_de_interes_mensual
          ) VALUES (
          {self.edad},
          {self.expectativa_vida},
          {self.años_renta},
          {self.total_cuotas},
          {self.precio_de_la_vivienda},
          {self.porcentaje_precio_real},
          {self.valor_de_la_hipoteca},
          {self.tasa_de_interes_mensual}
        );
        """)
        cursor.connection.commit()
    def BuscarUsuarioCedula( cedula ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorUsuario.ObtenerCursor()

        cursor.execute(f"""select cedula, expectativa_vida,años_renta,total_cuotas, precio_de_la_vivienda,porcentaje_precio_real,valor_de_la_hipoteca,
        tasa_de_interes_mensualfrom usuarios where cedula = '{cedula}'""" )
        fila = cursor.fetchone()
        resultado = Usuario( cedula=fila[0],expectativa_vida=fila[1], años_renta=fila[2],total_cuotas=fila[3],
                            precio_de_la_vivienda=fila[4],porcentaje_precio_real=fila[5],valor_de_la_hipoteca=fila[6],tasa_de_interes_mensual=fila[7]  )
        return resultado

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor