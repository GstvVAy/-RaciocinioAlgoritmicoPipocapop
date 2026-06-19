ingredientes = {}

def add_ingrediente(nome: str, quantidade: float, unidade: str = "un"):
	if nome in ingredientes:
		ingredientes[nome]["quantidade"] += quantidade
		if unidade:
			ingredientes[nome]["unidade"] = unidade
	else:
		ingredientes[nome] = {"quantidade": quantidade, "unidade": unidade}


def get_ingrediente(nome: str):
	return ingredientes.get(nome)


def list_ingredientes():
	return ingredientes


def subtrair_ingrediente(nome: str, quantidade: float):
	ingrediente = get_ingrediente(nome)
	if ingrediente is None:
		return False
	if quantidade > ingrediente["quantidade"]:
		return False
	ingrediente["quantidade"] -= quantidade
	return True


def tem_estoque_para(ingredientes_necessarios: dict):
	for nome, quantidade in ingredientes_necessarios.items():
		ingrediente = get_ingrediente(nome)
		if ingrediente is None or ingrediente["quantidade"] < quantidade:
			return False
	return True
