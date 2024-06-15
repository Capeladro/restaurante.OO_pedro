#questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

carro_1 = Carro('Jeep', 'Branco', 2020)
print(carro_1)

#questão 2
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.menu = None
        self.mesas = 0

#questão 4
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Menu: {self.menu}, Mesas: {self.mesas}"
    
#questão 3
restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.endereco = 'R. Uriel dos Reis, 45'
restaurante1.capacidade = 50
print(restaurante1)
#construtor
restaurante2 = Restaurante('Francesa', 'Italiana')
print(restaurante2)

#questão 5
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

cliente1 = Cliente('Eduarda Moro', 'eduarda.moro@escola.pr.gov.br', '1111-2222', 'Rua 1, 10')
cliente2 = Cliente('Heloise de Castro', 'heloise.castro@escola.pr.gov.br', '3333-4444', 'Rua 2, 20')
cliente3 = Cliente('Maria Jacomasso', 'maria.jacomasso@escola.pr.gov.br', '5555-6666', 'Rua 3, 30')

print(cliente1)
print(cliente2)
print(cliente3)