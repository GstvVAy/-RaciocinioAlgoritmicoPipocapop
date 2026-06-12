from .Produto import Produto


class GerenciadorProducao:
    def __init__(self):
        self.produtos = []
        self.tabela = []

    def adicionar_produto(self, id_produto: str, nome: str, ingredientes: dict, preco: float = 0.0):
        p = Produto(id_produto, nome, ingredientes, preco)
        self.produtos.append(p)
        self.tabela.append(f"|| ID:{p.id} || Nome:{p.nome} || Ingredientes:{p.ingredientes} || Preco:{p.preco} ||")
        return p

    def obter_ingredientes_produto(self, id_produto: str):
        for p in self.produtos:
            if p.id == id_produto:
                return dict(p.ingredientes)
        return None

    def listar_produtos(self):
        return [p.as_dict() for p in self.produtos]
