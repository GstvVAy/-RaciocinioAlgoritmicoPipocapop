class Produto:
    def __init__(self, id_produto: str, nome: str, ingredientes: dict, preco: float = 0.0):
        self.id = id_produto
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco = preco

    def as_dict(self):
        return {"id": self.id, "nome": self.nome, "ingredientes": self.ingredientes, "preco": self.preco}
