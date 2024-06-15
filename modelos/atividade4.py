
class Livro:
    livros = []

#questão 1
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

#questão 2
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Disponível: {self.disponivel}"

#questão 3
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

#questão 4
    @staticmethod
    def verificar_disponibilidade(ano):
        return [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]

if __name__ == "__main__":
    livro1 = Livro("Suicidas", "Raphael Montes", 2012)
    livro2 = Livro("Verity", "Colleen Hoover", 2018)


    print(livro1)
    print(livro2)


    livro1.emprestar()
    print(f"Após empréstimo, disponível: {livro1.disponivel}")


    ano_verificar = 1954
    livros_disponiveis = Livro.verificar_disponibilidade(ano_verificar)
    print(f"Livros disponíveis em {ano_verificar}:")
    for livro in livros_disponiveis:
        print(livro)