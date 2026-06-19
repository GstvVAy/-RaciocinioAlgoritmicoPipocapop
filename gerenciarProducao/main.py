from .Ingrediente import add_ingrediente, list_ingredientes, tem_estoque_para, subtrair_ingrediente
from .Linhadeproducao import GerenciadorProducao
from .Producao import Producao


class EstoqueProdutos:
    def __init__(self):
        self.itens = {}

    def adicionar_estoque(self, produto_id: str, quantidade: float):
        if produto_id in self.itens:
            self.itens[produto_id] += quantidade
        else:
            self.itens[produto_id] = quantidade

    def obter_quantidade(self, produto_id: str):
        return self.itens.get(produto_id, 0.0)

    def listar_estoque(self):
        return self.itens


class SistemaProducao:
    def __init__(self):
        self.gerenciador = GerenciadorProducao()
        self.estoque_produtos = EstoqueProdutos()
        self.producoes = []
        self.id_producao = 1

    def cadastrar_ingrediente(self):
        nome = input("Nome do ingrediente: ")
        quantidade = float(input("Quantidade inicial: "))
        unidade = input("Unidade (padrao 'un'): ") or "un"
        add_ingrediente(nome, quantidade, unidade)
        print("Ingrediente cadastrado com sucesso!")

    def cadastrar_produto(self):
        id_produto = input("ID do produto: ")
        nome = input("Nome do produto: ")
        preco = float(input("Preco do produto: "))

        print("Digite os ingredientes do produto. Informe 'fim' para encerrar.")
        ingredientes = {}
        while True:
            nome_ing = input("Ingrediente: ")
            if nome_ing.lower() == "fim":
                break
            quantidade = float(input("Quantidade por unidade do produto: "))
            ingredientes[nome_ing] = quantidade

        self.gerenciador.adicionar_produto(id_produto, nome, ingredientes, preco)
        print("Produto cadastrado com sucesso!")

    def registrar_producao(self):
        if len(self.gerenciador.produtos) == 0:
            print("Nenhum produto cadastrado. Cadastre um produto primeiro.")
            return

        for produto in self.gerenciador.produtos:
            print(f"ID: {produto.id} | Nome: {produto.nome} | Preco: R${produto.preco:.2f}")

        id_produto = input("ID do produto a produzir: ")
        produto = self.gerenciador.buscar_produto(id_produto)
        if produto is None:
            print("Produto nao encontrado.")
            return

        quantidade_produzida = float(input("Quantidade produzida: "))
        ingredientes_necessarios = produto.calcular_ingredientes_para_quantidade(quantidade_produzida)

        if not tem_estoque_para(ingredientes_necessarios):
            print("Estoque de ingredientes insuficiente para esta producao.")
            return

        for nome, quantidade in ingredientes_necessarios.items():
            subtrair_ingrediente(nome, quantidade)

        self.estoque_produtos.adicionar_estoque(produto.id, quantidade_produzida)
        metodo_producao = input("Metodo de producao: ")
        data = input("Data da producao: ")

        producao = Producao(self.id_producao, data, produto.id, quantidade_produzida, ingredientes_necessarios, metodo_producao)
        self.producoes.append(producao)
        self.id_producao += 1

        print("Producao registrada com sucesso!")

    def listar_ingredientes(self):
        itens = list_ingredientes()
        if len(itens) == 0:
            print("Nenhum ingrediente cadastrado.")
            return
        for nome, dados in itens.items():
            print(f"{nome}: {dados['quantidade']} {dados['unidade']}")

    def listar_produtos(self):
        produtos = self.gerenciador.listar_produtos()
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
            return
        for p in produtos:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Preco: R${p['preco']:.2f} | Ingredientes: {p['ingredientes']}")

    def listar_estoque(self):
        estoque = self.estoque_produtos.listar_estoque()
        if len(estoque) == 0:
            print("Nenhum produto em estoque.")
            return
        for produto_id, quantidade in estoque.items():
            print(f"Produto ID: {produto_id} | Quantidade em estoque: {quantidade}")

    def listar_producoes(self):
        if len(self.producoes) == 0:
            print("Nenhuma producao registrada.")
            return
        for p in self.producoes:
            print(f"ID: {p.id} | Produto ID: {p.produto_id} | Quantidade: {p.quantidade_produzida} | Data: {p.data} | Metodo: {p.metodo_producao} | Ingredientes usados: {p.ingredientes_usados}")

    def menu(self):
        while True:
            print("""
--- GERENCIAMENTO DE PRODUCAO ---
1 - Cadastrar ingrediente
2 - Cadastrar produto
3 - Registrar producao
4 - Listar ingredientes
5 - Listar produtos
6 - Listar estoque de produtos
7 - Listar producoes
8 - Sair
""")
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.cadastrar_ingrediente()
            elif opcao == "2":
                self.cadastrar_produto()
            elif opcao == "3":
                self.registrar_producao()
            elif opcao == "4":
                self.listar_ingredientes()
            elif opcao == "5":
                self.listar_produtos()
            elif opcao == "6":
                self.listar_estoque()
            elif opcao == "7":
                self.listar_producoes()
            elif opcao == "8":
                print("Sistema encerrado.")
                break
            else:
                print("Opcao invalida.")


if __name__ == "__main__":
    sistema = SistemaProducao()
    sistema.menu()
