import psycopg2
import SecretConfig
from model.model.resumen_financiero import ResumenFinanciero
class ResumenFinancieroController:
    def CrearTabla():
        cursor = ResumenFinancieroController.ObtenerCursor()
        with open("hipoteca_inversa/sql/crear_resumen_financiero.sql","r") as archivo :
            consulta=archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
    def eliminar_tabla():
        cursor=ResumenFinancieroController.ObtenerCursor()
        with open("hipoteca_inversa/sql/crear_resumen_financiero.sql","r") as archivo :
            consulta=archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
    def insertar_resumen(self):
        cursor=ResumenFinancieroController.ObtenerCursor()
        cursor.execute(f"""INSERT INTO resumen_financiero(
            id_pago,
            cedula,
            ingreso_mensual,
            deuda_total) VALUES(
            {self.id_pago},
            {self.cedula},
            {self.ingreso_mensual},
            {self.deuda_total});""")
        cursor.connection.commit()
    def buscar_id_pago(id_pago):
        cursor=ResumenFinancieroController.ObtenerCursor()
        cursor.execute("SELECT id_pago,cedula,ingreso_mensual,deuda_total from resumen_financiero where id_pago='{id_pago}'")
        fila = cursor.fetchone()
        resultado=ResumenFinanciero(id_pago=fila[0],cedula=fila[1],ingreso_mensual=fila[2],deuda_total=fila[3])
        return resultado
    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor