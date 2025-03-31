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
class app:
    def __init__(self,root):
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


        
#colocar um input aqui:
#autor1 = Autor(1, "Machado de Assis", "Brasileiro")
#autor2 = Autor(2, "Jane Austen", "Britânica")

# Salvando autores em json
#Autor.salvar_em_json([autor1, autor2])

# Carregar autores do arquivo json, transformar ou colar la na função
#autores_carregados = Autor.carregar_de_json()
#for autor in autores_carregados:
#    print(f"ID: {autor.id_autor}, Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}")

    root = tk.Tk()
    root.title("Autores")
    root.geometry("800x600")
    

    root.mainloop()
        