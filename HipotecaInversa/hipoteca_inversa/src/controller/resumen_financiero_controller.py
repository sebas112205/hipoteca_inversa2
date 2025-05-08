import psycopg2
import SecretConfig
class ResumenFinancieroController:
    def CrearTabla():
        cursor = ResumenFinancieroController.ObtenerCursor()
        cursor.execute("""CREATE TABLE resumen_financiero (
    id_pago SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL,
    ingreso_mensual DECIMAL(15, 2) NOT NULL,
    deuda_total DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (cedula) REFERENCES usuarios(cedula)
);""")
        cursor.connection.commit()
    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor