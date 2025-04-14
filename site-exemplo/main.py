import tkinter as tk
from tkinter import messagebox
from Livro import Livro
from Usuario import Usuario
from Livro import Biblioteca
from Livro import App

def adicionar_usuario():

    adicionar_usuario_janela = tk.Toplevel(root)
    adicionar_usuario_janela.title("Adicionar Usuário")
    adicionar_usuario_janela.geometry("300x250")

    def salvar_usuario(entry_nome, entry_email, entry_genero, entry_idade):
        nome = entry_nome.get()
        email = entry_email.get()
        genero = entry_genero.get()
        idade = entry_idade.get()

        user = Usuario(nome, idade,email)

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(user, autores, f, indent=4, ensure_ascii=False)

        if nome and email and genero and idade:
            lista_usuarios.insert(tk.END, f"Nome: {nome}, Email: {email}, Gênero: {genero}, Idade: {idade}")
            adicionar_usuario_janela.destroy() 
        else:
            messagebox.showwarning("Campos incompletos", "Preencha todos os campos")

    
    tk.Label(adicionar_usuario_janela, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(adicionar_usuario_janela)
    entry_nome.pack(pady=5)

    tk.Label(adicionar_usuario_janela, text="Email:").pack(pady=5)
    entry_email = tk.Entry(adicionar_usuario_janela)
    entry_email.pack(pady=5)

    tk.Label(adicionar_usuario_janela, text="Gênero:").pack(pady=5)
    entry_genero = tk.Entry(adicionar_usuario_janela)
    entry_genero.pack(pady=5);

    tk.Label(adicionar_usuario_janela, text="Idade:").pack(pady=5)
    entry_idade = tk.Entry(adicionar_usuario_janela)
    entry_idade.pack(pady=5)

    tk.Button(adicionar_usuario_janela, text="Salvar", command=salvar_usuario(entry_email, entry_nome, entry_genero, entry_idade)).pack(pady=10)




def __init__(self):
        self.livros = []

def adicionar_livro(self, titulo, genero):
        self.livros.append(Livro(titulo, genero))

def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return (f"O livro '{titulo}' foi emprestado com sucesso!"
                        if livro.emprestar() else
                        f"O livro '{titulo}' não está disponível no momento.")
        return f"O livro '{titulo}' não foi encontrado na biblioteca."

def adicionar_livro__init__(self, root):
    self.root = root
    self.root.title("Biblioteca")
    self.root.geometry("800x600")

def salvar_livro():
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.disponivel = True

def abrir_janela_adicionar_livro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Livro")
        janela.geometry("400x300")

        tk.Label(janela, text="Título").pack(pady=5)
        entry_titulo = tk.Entry(janela)
        entry_titulo.pack(pady=5)

        tk.Label(janela, text="Gênero").pack(pady=5)
        entry_genero = tk.Entry(janela)
        entry_genero.pack(pady=5)  

        def salvar_livro():
            titulo = entry_titulo.get()
            genero = entry_genero.get()
            self.biblioteca.adicionar_livro(titulo, genero)
            janela.destroy()      

        tk.Button(janela, text="Salvar", command=salvar_livro).pack(pady=20)   

def abrir_janela_emprestar_livro(self):
        janela = tk.Toplevel(self.root)
        janela.title("Emprestar Livro")
        janela.geometry("400x400")

        

#def adicionar_autor():
#    adicionar_autor_janela = tk.Toplevel(root)
#   adicionar_autor_janela.title = ("Adicionar Autor")
#   adicionar_autor_janela.geometry = ("300x250")


def status_livro():
    status_livro_janela = tk.Toplevel(root)
    status_livro_janela.title = ("Status do Livro")
    status_livro_janela.geometry = ("300x250")

root = tk.Tk()
root.title("Biblioteca")
root.geometry("800x600")
root.config(bg="#ADD8E6")

tk.Button(root, text="Adicionar Livro", width=20, command=abrir_janela_adicionar_livro).pack(pady=10)
#tk.Button(root, text="Adicionar Autor", width=20, command=adicionar_autor).pack(pady=10)
tk.Button(root, text="Adicionar Usuário", width=20, command=adicionar_usuario).pack(pady=10)
tk.Button(root, text="Status de Livro", width=20, command=status_livro).pack(pady=10)


tk.Label(root, text="Lista de Usuários", font=("Arial", 14)).pack(pady=20)
lista_usuarios = tk.Listbox(root, width=100, height=15)
lista_usuarios.pack()

root.mainloop()
