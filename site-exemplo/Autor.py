import json
import tkinter as tk

class Autor:
    def __init__(self, id_autor: int, nome: str, nacionalidade: str):
        self.id_autor = id_autor
        self.nome = nome
        self.nacionalidade = nacionalidade

    def para_dicionario(self):
        return{
            "id_autor": self.id_autor,
            "nome": self.nome,
            "nacionalidade": self.nacionalidade}
    

    def salvar_em_json(autores, arquivo="autores.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([autor.para_dicionario() for autor in autores], f, indent=4, ensure_ascii=False)
    
    def do_dicionario(cls, dados):
        return cls(id_autor=dados["id_autor"],nome=dados["nome"], nacionalidade=dados["nacionalidade"])

    def carregar_de_json(arquivo="autores.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Autor.do_dicionario(autor) for autor in dados]
        except FileNotFoundError:
            return print("O arquivo não foi encontrado")
        
#colocar um input aqui:

autor3 = Autor(3, "Shakespare", "Romano" )
#Salvando autores em json
Autor.salvar_em_json([autor3])

# Carregar autores do arquivo json
autores_carregados = Autor.carregar_de_json()
for autor in autores_carregados:
    print(f"ID: {autor.id_autor}, Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}")


def cadastrar_autor(arquivo="autores.json"):
        autores = Autor.carregar_de_json(arquivo)



        nome = input("Digite o nome do autor: ")
        nacionalidade = input("Digite a nacionalidade do autor: ")

        novo_autor = Autor(novo_id, nome, nacionalidade)
        autores.append(novo_autor)

        Autor.salvar_em_json(autores, arquivo)
       print(f"Autor {nome} cadastrado com sucesso!")

"""class app:
    def init(self,root):
        self.root = root
        self.root.title("Adicionar Autores")
        self.root.geometry("800x600")

        self.autor = Autor() 
        self.botao_adicionar = tk.Button(self.root, text="Adicionar Autor", command=self.abrir_janela_adicionar_autor)
        self.botao_adicionar.pack(pady=20)

    def abrir_janela_adicionar_autor(self):
        adicionar_autor = tk.Toplevel(self.root)
        adicionar_autor.title("Adicionar Autor")
        adicionar_autor.geometry("400x300")

        tk.Label(adicionar_autor, text="Título").pack(pady=5)
        entry_titulo = tk.Entry(adicionar_autor)
        entry_titulo.pack(pady=5)

        tk.Label(adicionar_autor, text="Gênero").pack(pady=5)
        entry_genero = tk.Entry(adicionar_autor)
        entry_genero.pack(pady=5)


     root = tk.Tk()
    root.title("Autores")
    root.geometry("800x600")


    root.mainloop() """

        