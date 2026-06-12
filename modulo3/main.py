from inputs import entradas 
Manager = entradas()
while True:
    print("['add' para registrar operação] ['tabela' para retornar tabela] ['0' para encerrar]")
    main = Manager.perguntar("> ")
    Manager.checar_resposta(main)
