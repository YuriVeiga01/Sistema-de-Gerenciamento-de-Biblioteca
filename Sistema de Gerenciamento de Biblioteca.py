class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("Lista de Livros:")
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"O livro '{livro.titulo}' foi emprestado.")
                return
        print("Livro não encontrado ou indisponível.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"O livro '{livro.titulo}' foi devolvido.")
                return
        print("Livro não encontrado ou já está disponível.")

# Exemplo de uso
biblioteca = Biblioteca()

livro1 = Livro("Python Programming", "John Smith", 2020)
livro2 = Livro("Data Science Handbook", "Alice Johnson", 2019)
livro3 = Livro("Machine Learning Basics", "Bob Brown", 2018)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()

biblioteca.emprestar_livro("Python Programming")
biblioteca.emprestar_livro("Data Science Handbook")

biblioteca.listar_livros()

biblioteca.devolver_livro("Python Programming")

biblioteca.listar_livros()
