import psycopg2

# Reemplace los datos de conexion con los datos tomados de su servidor
connection = psycopg2.connect(database="neondb", user="Sebastian", password="npg_0slCze2StFhJ", host="ep-gentle-bush-a4p9wuaz-pooler.us-east-1.aws.neon.tech", port=10001)

# Todas las instrucciones se ejecutan a tavés de un cursor
cursor = connection.cursor()
cursor.execute("SELECT * from usuario;")

# Si la instruccion retorna resultados, se accede a ellos con fetchone() o fetchall()  segun la necesidad
record = cursor.fetchall()

print("Resultados : ")

# El resultado de fetchall() es una lista de tuplas
print(record)