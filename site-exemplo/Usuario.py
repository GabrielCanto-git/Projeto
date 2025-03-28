import tkinter as tk

class Usuario:
    def __init__(self, nome, idade, email, cpf):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

class Adicionar_Usuario:
    def __init__(self):
        self.usuario = []

    def adicionar_usuario(self, nome, idade, email, cpf):
        novo_usuario = Usuario(nome, email, idade, cpf)
        self.usuario.append(novo_usuario)

class Janela:
    def __init__(self,root):
        self.root = root
        self.root.title("Adicionar Usuarios")
        self.root.geometry("800x600")

        self.adicionar_usuario = Adicionar_Usuario()

        self.botao_adicionar = tk.Button(self.root, text= "Adicionar Usuario", command= self.abrir_janela_adicionar_usuario)
        self.botao_adicionar.pack(pady= 20)

    def abrir_janela_adicionar_usuario(self):
        adicionar_usuario_janela = tk.Toplevel(self.root)
        adicionar_usuario_janela.title = ("Adicionar Usuario")
        adicionar_usuario_janela.geometry = ("600x500")

        tk.Label(adicionar_usuario_janela, text="Nome").pack(pady=5)
        entry_nome = tk.Entry(adicionar_usuario_janela)
        entry_nome.pack(pady=5)

        tk.Label(adicionar_usuario_janela, text="Idade").pack(pady=5)
        entry_idade = tk.Entry(adicionar_usuario_janela)
        entry_idade.pack(pady=5)

        tk.Label(adicionar_usuario_janela, text="E-mail").pack(pady=5)
        entry_email = tk.Entry(adicionar_usuario_janela)
        entry_email.pack(pady=5)

        tk.Label(adicionar_usuario_janela, text="Cpf").pack(pady=5)
        entry_cpf = tk.Entry(adicionar_usuario_janela)
        entry_cpf.pack(pady=5)

        def salvar_usuario():
            nome = entry_nome.get()
            idade = entry_idade.get()
            email = entry_email.get()
            cpf = entry_cpf.get()
            self.adicionar_usuario.adicionar_usuario(nome, idade, email, cpf)
            adicionar_usuario_janela.destroy()  

        botao_salvar = tk.Button(adicionar_usuario_janela, text="Salvar", command=salvar_usuario)
        botao_salvar.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    Janela = Janela(root)
    root.mainloop()
