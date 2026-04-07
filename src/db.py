import psycopg

conn = psycopg.connect(
    "host=localhost port=5433 dbname=proyecto user=admin password=admin"
)

print("Conectado 🚀")