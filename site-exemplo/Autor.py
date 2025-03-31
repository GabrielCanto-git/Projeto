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

#
    def carregar_de_json(arquivo="autores.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Autor.do_dicionario(autor) for autor in dados]
        except FileNotFoundError:
            return print("O arquivo não foi encontrado")
        
#colocar um input aqui:
autor1 = Autor(1, "Machado de Assis", "Brasileiro")
autor2 = Autor(2, "Jane Austen", "Britânica")

#Salvando autores em json
Autor.salvar_em_json([autor1, autor2])

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


        