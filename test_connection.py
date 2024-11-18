import pg8000

try:
    conn = pg8000.connect(
        database="plataforma_todo",
        user="seu_usuario",
        password="sua_senha",
        host="localhost",
        port=5432
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
