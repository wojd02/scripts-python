class Mercado:
    taxa = 1.20

    def __init__(self, valor: float) -> None:
        self.valor_produto_bruto = valor

    def valor_do_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f"valor produto: {valor_produto}")
    @classmethod
    def editar_taxa(cls, valor: float):
        cls.taxa = valor

loja_1 = Mercado(30.50)
loja_2 = Mercado(10.39)
loja_3 = Mercado(20.33)

loja_1.valor_do_produto()
loja_2.valor_do_produto()
loja_3.valor_do_produto()


loja_1.editar_taxa(1.45) #Alterando com o método de classe e mantendo o SOLID
loja_1.taxa = 1.76 # alterando apenas para uma loja mas perdendo o SOLID

print("Valores pós aumento da Taxa")

loja_1.valor_do_produto()
loja_2.valor_do_produto()
loja_3.valor_do_produto()