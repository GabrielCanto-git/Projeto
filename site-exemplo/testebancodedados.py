import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Note_do_Gabs\SQLEXPRESS01;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()  #É um elemento que vai executar os comandos em sql no banco de dados

comando = """INSERT INTO autor(id, nome, livros)
    VALUES
	    (?,?,?)"""


cursor.execute(comando)#comando que executa
cursor.commit()#Só precisa disso caso o comando edite o banco de dados

#Função para o botão de adicionar o usuario
#def cadastrar_usuario(self, nome, email, genero, idade):
#   
#
#

        




