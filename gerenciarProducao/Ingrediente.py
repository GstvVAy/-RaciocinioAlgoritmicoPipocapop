ingredientes = {}

def add_ingrediente(nome: str, quantidade: float, unidade: str = "un"):
	ingredientes[nome] = {"quantidade": quantidade, "unidade": unidade}

def get_ingrediente(nome: str):
	return ingredientes.get(nome)

def list_ingredientes():
	return ingredientes
