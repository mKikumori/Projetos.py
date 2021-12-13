class Restaurante:

    def __init__(self, nome, mesas, garcons, ano):
        self.nome = nome
        self.mesas = mesas
        self.garcons = garcons
        self.ano = ano
        self._avaliacao = 0

    @property
    def avaliacao(self):
        return self._avaliacao

    def avaliar(self):
        self._avaliacao += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f"{self.nome}, {self.mesas}, {self.garcons}, {self.ano}, {self.avaliacao}"

class Pedido():
    def __init__(self, entrada, bebida, prato_principal, sobremesa):
        self.entrada = entrada
        self.bebida = bebida
        self.prato_principal = prato_principal
        self.sobremesa = sobremesa
        self.preco_entradas = 35
        self.preco_bebidas = 15
        self.preco_pratos_principais = 90
        self.preco_sobremesas = 13
        self._preco_total = 153

    @property
    def conta(self):
        return self._preco_total

    def __str__(self):
        return f"{self.entrada}, {self.bebida}, {self.prato_principal}, {self.sobremesa}"


pedido1 = Pedido("bolinha de bacalhau", "vinho tinto", "lasanha", "pudim de passas")
pedido2 = Pedido("tulipa", "suco de laranja", "picanha", "sorvete")
pedido3 = Pedido("salada", "agua", "sopa", "mix de frutas")
gustous = Restaurante("gustou's", 45, 25, 1974)
gustous.avaliar()
gustous.avaliar()

total_de_pedidos = [pedido1, pedido2, pedido3]
conta = 153 * len(total_de_pedidos)
print(gustous)
for pedidos_totais in total_de_pedidos:
    print(f"Foram pedidos: {pedidos_totais}")
print(f"Total: R$ {conta}")
