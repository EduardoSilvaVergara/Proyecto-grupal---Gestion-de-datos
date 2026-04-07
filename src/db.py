import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="proyecto",
    user="admin",
    password="admin"
)
print("Conectado")