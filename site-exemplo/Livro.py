import tkinter as tk

class Livro:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False  
            return True
        else:
            return False  


class Livro:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False


class Biblioteca:
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


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("800x600")

        self.biblioteca = Biblioteca()

        tk.Button(self.root, text="Adicionar Livro", command=self.abrir_janela_adicionar_livro).pack(pady=20)
        tk.Button(self.root, text="Emprestar Livro", command=self.abrir_janela_emprestar_livro).pack(pady=20)

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

        canvas = tk.Canvas(janela)
        scrollbar = tk.Scrollbar(janela, orient="vertical", command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.atualizar_lista_livros(frame)

        tk.Label(janela, text="Título do Livro").pack(pady=5)
        entry_titulo_emprestar = tk.Entry(janela)
        entry_titulo_emprestar.pack(pady=5)

        resultado_label = tk.Label(janela, text="")
        resultado_label.pack(pady=5)

        def emprestar():
            titulo = entry_titulo_emprestar.get()
            resultado = self.biblioteca.emprestar_livro(titulo)
            resultado_label.config(text=resultado)
            self.atualizar_lista_livros(frame)

        tk.Button(janela, text="Emprestar", command=emprestar).pack(pady=10)

    def atualizar_lista_livros(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        for livro in self.biblioteca.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            texto = f"{livro.titulo} ({livro.genero}) - {status}"
            tk.Label(frame, text=texto, anchor="w").pack(fill="x", padx=5, pady=2)

        frame.update_idletasks()
        frame.master.config(scrollregion=frame.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
