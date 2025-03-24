import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost\SQLEXPRESS01;Database=master;Trusted_Connection=True;"
    "Database=SistemaBiblioteca;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

comando = """INSERT INTO  Usuarios(id, nome, email, telefone)
VALUES 
	(1, 'Roberto', 'roberto@hotmail.com', 249)"""

cursor.execute(comando)
cursor.commit()
