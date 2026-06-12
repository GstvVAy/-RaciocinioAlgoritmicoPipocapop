from ops import ops
class entradas:
    def __init__(self):
        self.tabela = []
   
    def perguntar(self,pergunta):
        resposta = input(pergunta)
        return resposta 
   
    def checar_resposta(self,resposta):
        match resposta:
            case "add":
                idp = self.perguntar("Digite o ID do prouto: ")
                quantidade = int(self.perguntar("Digite a quantidade do prouto: "))
                matriz = {}
                while True:
 #pra quem for ler isso, essa parte deve ser substituida. Os itens e valores devem ser depositados automaticamente, devem ser buscandos pelo o id definido anteriormente 
                    nome = self.perguntar("Digite um dos máterial necessários:")
                    quant = int(self.perguntar("Digite a quantidade necessária do máterial para uma unidade:  "))
                    matriz[nome] = quant
                    final = self.perguntar("Digite 'e' para encerrar, e Enter para adicionar mais: ")
                    if final == "e":
                        break
                deltaTempo = int(self.perguntar("Digite o periodo de tempo(meses) da amostragem de venda: "))
                novoProduto = ops(idp,quantidade,matriz, deltaTempo)
                self.tabela.append([f"|| ID:{novoProduto.idp} || Vendido:{novoProduto.quant} || Débito máterial:{novoProduto.material()} || Projeção de estoque:{novoProduto.demanda()} || Projeção de reserva:{novoProduto.reserva()} || "])
                return print("Adição bem sucedida")
           
            case "tabela":
                return print(self.tabela)

            case"0":
                return exit()            

