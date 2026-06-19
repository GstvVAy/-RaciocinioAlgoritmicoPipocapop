import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Produto:
    def __init__(self, id, nome, valor):
        self.id = id
        self.nome = nome
        self.valor = valor


from gerenciarProducao.main import SistemaProducao


class Venda:
    def __init__(self, id, produto, cliente, quantidade, data):
        self.id = id
        self.produto = produto
        self.cliente = cliente
        self.quantidade = quantidade
        self.data = data
        self.valor_total = produto.valor * quantidade


class SistemaVendas:
    def __init__(self, sistema_producao=None):
        self.clientes = []
        self.vendas = []
        self.id_venda = 1
        self.sistema_producao = sistema_producao or SistemaProducao()

        self.produtos = [
            Produto(1, "Pipoca Doce", 8.00),
            Produto(2, "Pipoca Salgada", 7.00),
            Produto(3, "Pipoca Gourmet", 12.00),
            Produto(4, "Pipoca Caramelizada", 10.00)
        ]

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")

        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)

        print("Cliente cadastrado com sucesso!")

    def listar_produtos(self):
        print("\n--- PRODUTOS DISPONÍVEIS ---")

        for produto in self.produtos:
            quantidade_estoque = self.sistema_producao.estoque_produtos.obter_quantidade(produto.id)
            print(f"ID: {produto.id} | Nome: {produto.nome} | Valor: R${produto.valor:.2f} | Estoque: {quantidade_estoque}")

    def buscar_cliente(self, nome_cliente):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome_cliente.lower():
                return cliente

        return None

    def buscar_produto(self, id_produto):
        for produto in self.produtos:
            if produto.id == id_produto:
                return produto

        return None

    def registrar_venda(self):
        if len(self.clientes) == 0:
            print("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
            return

        nome_cliente = input("Digite o nome do cliente: ")
        cliente = self.buscar_cliente(nome_cliente)

        if cliente == None:
            print("Cliente não encontrado.")
            return

        self.listar_produtos()

        id_produto = int(input("Digite o ID do produto vendido: "))
        quantidade = int(input("Digite a quantidade vendida: "))
        data = input("Digite a data da venda: ")

        produto = self.buscar_produto(id_produto)

        if produto == None:
            print("Produto não encontrado.")
            return

        estoque_disponivel = self.sistema_producao.estoque_produtos.obter_quantidade(produto.id)
        if quantidade > estoque_disponivel:
            print(f"Estoque insuficiente. Disponível: {estoque_disponivel}")
            return

        venda = Venda(self.id_venda, produto, cliente, quantidade, data)
        self.vendas.append(venda)

        self.id_venda += 1

        print("Venda registrada com sucesso!")
        print(f"Valor total da venda: R${venda.valor_total:.2f}")

    def listar_vendas(self):
        print("\n--- VENDAS REGISTRADAS ---")

        if len(self.vendas) == 0:
            print("Nenhuma venda registrada.")
            return

        for venda in self.vendas:
            print(f"""
ID da venda: {venda.id}
Produto ID: {venda.produto.id}
Produto: {venda.produto.nome}
Cliente: {venda.cliente.nome}
Quantidade vendida: {venda.quantidade}
Valor: R${venda.valor_total:.2f}
Data: {venda.data}
""")

    def menu(self):
        while True:
            print("""
--- GERENCIAMENTO DE VENDAS ---
Fábrica de Pipoca - Loja Própria

1 - Cadastrar cliente
2 - Listar produtos
3 - Registrar venda
4 - Listar vendas
5 - Sair
""")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_cliente()
            elif opcao == "2":
                self.listar_produtos()
            elif opcao == "3":
                self.registrar_venda()
            elif opcao == "4":
                self.listar_vendas()
            elif opcao == "5":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")


def main(sistema_producao=None):
    sistema = SistemaVendas(sistema_producao)
    sistema.menu()


if __name__ == "__main__":
    main()
