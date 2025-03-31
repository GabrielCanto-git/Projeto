import json
import tkinter as tk

class Autor:
    def __init__(self, nome: str, nacionalidade: str):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
    
    def id_autor(self):
        return self.__id_autor

    def nome(self):
        return self.__nome
    
    def nacionalidade(self):
        return self.__nacionalidade

    def para_dicionario(self):
        return{
            "id_autor": self.__id_autor,
            "nome": self.__nome,
            "nacionalidade": self.__nacionalidade
        }


    def salvar_em_json(autores, arquivo="autores.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([autor.para_dicionario() for autor in autores], f, indent=4, ensure_ascii=False)

    def carregar_de_json(arquivo="autores.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Autor.from_dict(autor) for autor in dados]
        except FileNotFoundError:
            return []
        
#colocar um input aqui:
#autor1 = Autor(1, "Machado de Assis", "Brasileiro")
#autor2 = Autor(2, "Jane Austen", "Britânica")

# Salvando autores em json
#Autor.salvar_em_json([autor1, autor2])

# Carregar autores do arquivo json, transformar ou colar la na função
#autores_carregados = Autor.carregar_de_json()
#for autor in autores_carregados:
#    print(f"ID: {autor.id_autor}, Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}")


        