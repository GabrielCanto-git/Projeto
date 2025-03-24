import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Note_do_Gabs\SQLEXPRESS01;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()
comando = """INSERT INTO  Usuarios(id, nome, email, telefone)
VALUES 
	(2, 'roberto', 'roberto@hotmail.com', 232)"""

cursor.execute(comando)
cursor.commit()

