import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Note_do_Gabs\SQLEXPRESS01;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()  #É um elemento que vai executar os comandos em sql no banco de dados

comando = """INSERT INTO Usuarios(id, nome, email, telefone)
VALUES
	(2, 'roberto', 'roberto@hotmail.com', 232)"""

cursor.execute(comando)#comando que executa
cursor.commit()#Só precisa disso caso o comando edite o banco de dados

#sd
#teste