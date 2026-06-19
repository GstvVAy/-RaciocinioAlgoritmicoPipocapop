class Producao:
    def __init__(self, id_producao: int, data: str, produto_id: str, quantidade_produzida: float, ingredientes_usados: dict, metodo_producao: str):
        self.id = id_producao
        self.data = data
        self.produto_id = produto_id
        self.quantidade_produzida = quantidade_produzida
        self.ingredientes_usados = ingredientes_usados
        self.metodo_producao = metodo_producao

    def as_dict(self):
        return {
            "id": self.id,
            "data": self.data,
            "produto_id": self.produto_id,
            "quantidade_produzida": self.quantidade_produzida,
            "ingredientes_usados": self.ingredientes_usados,
            "metodo_producao": self.metodo_producao,
        }
