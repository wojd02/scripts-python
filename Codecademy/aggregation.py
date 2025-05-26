class Produto:
    def __init__(self, nome: str, preço: float) -> None:
        self.__nome = nome
        self.__preço = preço

    def infos_produto(self) -> None:
        print(f'Produto - {self.__nome} Preço - {self.__preço}')

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
    def adicionar_produto(self, produto: Produto):
        self.__produtos.append(produto)
    def finalizar_compra(self) -> None:
        for prod in self.__produtos:
            prod.infos_produto()

Banana = Produto('Banana', 13.50)
Uva = Produto('Uva', 4.25)
Pera = Produto('Pera', 9.20)

Carrinho = CarrinhoDeCompras()

Carrinho.adicionar_produto(Banana)
Carrinho.adicionar_produto(Uva)
Carrinho.adicionar_produto(Pera)

Carrinho.finalizar_compra()