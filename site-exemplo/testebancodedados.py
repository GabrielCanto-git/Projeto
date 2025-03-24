import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost\SQLEXPRESS01;Database=master;Trusted_Connection=True;"
    "Database=SistemaBiblioteca;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()