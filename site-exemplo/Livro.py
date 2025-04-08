import tkinter as tk
import json



class Livro:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False  # O livro agora está emprestado
            return True
        else:
            return False  # O livro não está disponível 

    def dicionario(self):
        return {
            'titulo': self.titulo,
            'genero': self.genero
        }
    def do_dicionario(cls, dados):
        return cls(dados["titulo"], dados["genero"], dados["disponivel"])




class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, genero):
       novo_livro = Livro(titulo, genero)
       self.novo_livro.append(novo_livro)

    def salvar_emjson(self, arquivo="biblioteca.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
             json.dump([livro.dicionario() for livro in self.livros], f, indent=4, ensure_ascii=False)


    def carregar_de_json(self, arquivo="biblioteca.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.livros = [Livro.do_dicionario(d) for d in dados]
        except FileNotFoundError:
            print("Arquivo não encontrado")



    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    return f"O livro '{titulo}' foi emprestado com sucesso!"
                else:
                    return f"O livro '{titulo}' não está disponível no momento."
        return f"O livro '{titulo}' não foi encontrado na biblioteca."    


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Adicionar Livros")
        self.root.geometry("800x600")

        self.biblioteca = Biblioteca()

        self.botao_adicionar = tk.Button(self.root, text="Adicionar Livro", command=self.abrir_janela_adicionar_livro)
        self.botao_adicionar.pack(pady=20)
        self.botao_emprestar = tk.Button(self.root, text="Emprestar Livro", command=self.abrir_janela_emprestar_livro)
        self.botao_emprestar.pack(pady=20)

    def abrir_janela_adicionar_livro(self):
        adicionar_livro_janela = tk.Toplevel(self.root)
        adicionar_livro_janela.title("Adicionar Livros")
        adicionar_livro_janela.geometry("400x300")

        tk.Label(adicionar_livro_janela, text="Título").pack(pady=5)
        entry_titulo = tk.Entry(adicionar_livro_janela)
        entry_titulo.pack(pady=5)

        tk.Label(adicionar_livro_janela, text="Gênero").pack(pady=5)
        entry_genero = tk.Entry(adicionar_livro_janela)
        entry_genero.pack(pady=5)

        def salvar_livro():
            titulo = entry_titulo.get()
            genero = entry_genero.get()
            self.biblioteca.adicionar_livro(titulo, genero)
            adicionar_livro_janela.destroy()  

        botao_salvar = tk.Button(adicionar_livro_janela, text="Salvar", command=salvar_livro)
        botao_salvar.pack(pady=20)

    def abrir_janela_emprestar_livro(self):
        emprestar_livro_janela = tk.Toplevel(self.root)
        emprestar_livro_janela.title("Emprestar Livro")
        emprestar_livro_janela.geometry("300x200")

        canvas = tk.Canvas(emprestar_livro_janela)
        scrollbar = tk.Scrollbar(emprestar_livro_janela, orient="vertical", command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)

        canvas.create_window((0, 0), window=frame, anchor="nw")

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.atualizar_lista_livros(frame)

        tk.Label(emprestar_livro_janela, text="Título do Livro").pack(pady=5)
        entry_titulo_emprestar = tk.Entry(emprestar_livro_janela)
        entry_titulo_emprestar.pack(pady=5)

    def emprestar():
        titulo = entry_titulo_emprestar.get()
        resultado = self.biblioteca.emprestar_livro(titulo)
            # Exibir mensagem de sucesso ou falha
        resultado_label.config(text=resultado)

        tk.Label(emprestar_livro_janela, text="Título do Livro").pack(pady=5)
        entry_titulo_emprestar = tk.Entry(emprestar_livro_janela)
        entry_titulo_emprestar.pack(pady=5)

    def atualizar_lista_livros(self, frame):
        # Limpa a lista de livros no frame
            for widget in frame.winfo_children():
                widget.destroy()

        # Exibe os livros disponíveis com rolagem
            for livro in self.biblioteca.livros:
                texto = f"{livro.titulo} ({livro.genero}) - {'Disponível' if livro.disponivel else 'Emprestado'}"
                livro_label = tk.Label(frame, text=texto, anchor="w")
                livro_label.pack(fill="x", padx=5, pady=2)

        # Atualiza o tamanho do canvas para ajustar os itens
            frame.update_idletasks()
            frame.config(height=len(self.biblioteca.livros)*30)
            frame.master.config(scrollregion=frame.bbox("all"))

            botao_emprestar = tk.Button(emprestar_livro_janela, text="Emprestar", command=emprestar)
            botao_emprestar.pack(pady=20)

            resultado_label = tk.Label(emprestar_livro_janela, text="")
            resultado_label.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
