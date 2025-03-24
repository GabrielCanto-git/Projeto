import tkinter as tk
from tkinter import messagebox

def adicionar_usuario():

    adicionar_usuario_janela = tk.Toplevel(root)
    adicionar_usuario_janela.title("Adicionar Usuário")
    adicionar_usuario_janela.geometry("300x250")

    def salvar_usuario():
        nome = entry_nome.get()
        email = entry_email.get()
        genero = entry_genero.get()
        idade = entry_idade.get()

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
    entry_genero.pack(pady=5)

    tk.Label(adicionar_usuario_janela, text="Idade:").pack(pady=5)
    entry_idade = tk.Entry(adicionar_usuario_janela)
    entry_idade.pack(pady=5)

    tk.Button(adicionar_usuario_janela, text="Salvar", command=salvar_usuario).pack(pady=10)

def adicionar_livro():
    adicionar_livro_janela = tk.Toplevel(root)
    adicionar_livro_janela.title =("Adicionar Livros")
    adicionar_livro_janela.geometry = ("300x250")


def adicionar_autor():
    adicionar_autor_janela = tk.Toplevel(root)
    adicionar_autor_janela.title = ("Adicionar Autor")
    adicionar_autor_janela.geometry = ("300x250")


def status_livro():
    status_livro_janela = tk.Toplevel(root)
    status_livro_janela.title = ("Status do Livro")
    status_livro_janela.geometry = ("300x250")

root = tk.Tk()
root.title("Biblioteca")
root.geometry("800x600")
root.config(bg="#ADD8E6")

tk.Button(root, text="Adicionar Livro", width=20, command=adicionar_livro).pack(pady=10)
tk.Button(root, text="Adicionar Autor", width=20, command=adicionar_autor).pack(pady=10)
tk.Button(root, text="Adicionar Usuário", width=20, command=adicionar_usuario).pack(pady=10)
tk.Button(root, text="Status de Livro", width=20, command=status_livro).pack(pady=10)


tk.Label(root, text="Lista de Usuários", font=("Arial", 14)).pack(pady=20)
lista_usuarios = tk.Listbox(root, width=100, height=15)
lista_usuarios.pack()

root.mainloop()
