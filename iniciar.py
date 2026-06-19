import os
import subprocess
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, ROOT_DIR)

from gerenciarProducao.main import SistemaProducao
from modulovendas.script import main as vendas_main


def run_gerenciar_producao(sistema_producao):
    sistema_producao.menu()


def run_modulovendas(sistema_producao):
    vendas_main(sistema_producao)


def run_modulo3():
    script_path = os.path.join(ROOT_DIR, "modulo3", "main.py")
    return subprocess.run([sys.executable, script_path], cwd=ROOT_DIR)


def main():
    sistema_producao = SistemaProducao()

    while True:
        print("""
--- MENU PRINCIPAL ---
1 - Gerenciar produção
2 - Sistema de vendas
3 - Módulo 3
4 - Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            run_gerenciar_producao(sistema_producao)
        elif opcao == "2":
            run_modulovendas(sistema_producao)
        elif opcao == "3":
            run_modulo3()
        elif opcao == "4":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
