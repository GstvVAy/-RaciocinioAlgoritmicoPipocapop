from .Ingrediente import get_ingrediente


class Produto:
    def __init__(self, id_produto: str, nome: str, ingredientes: dict, preco: float = 0.0):
        self.id = id_produto
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco = preco

    def as_dict(self):
        return {"id": self.id, "nome": self.nome, "ingredientes": self.ingredientes, "preco": self.preco}

    def ingredientes_reais(self):
        return {nome: get_ingrediente(nome) for nome in self.ingredientes}

    def calcular_ingredientes_para_quantidade(self, quantidade: float):
        return {nome: quantidade * valor for nome, valor in self.ingredientes.items()}
