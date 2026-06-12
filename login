import sqlite3
import random


User = sqlite3.connect("User.db")
mensager = User.cursor()

mensager.execute("CREATE TABLE IF NOT EXISTS Usuarios ( ID INTEGER NOT NULL PRIMARY KEY UNIQUE, Username TEXT NOT NULL, Senha INTEGER NOT NULL)")


class UserManager:
    def _init_(self):
        pass
    
    def inserir(self):
        while True:
            id = random.randint(1111,9999)
            idigual = "SELECT ID FROM Usuarios WHERE ID = ?"
            mensager.execute(idigual,(id,))
            id_check = mensager.fetchall()
            if id_check == (id,):
                pass
            else:
                break
        
        nome = input("insira seu nome: ")
        senha = int(input("insira sua senha: "))
        inserir = "INSERT INTO Usuarios (ID,Username,Senha) Values(?,?,?)"
        mensager.execute(inserir,(id,nome,senha))       
        User.commit()
        User.close()
        print("Usuário cadástrado com sucesso")


    def login(self):
        nome = input("Username: ")
        senha = int(input("senha: "))
        nameV = "SELECT Username FROM Usuarios WHERE Username = (?)"
        mensager.execute(nameV,(nome,))
        nome_check = mensager.fetchall()

        senhaV = "SELECT Senha FROM Usuarios WHERE Username = (?)"
        mensager.execute(senhaV,(nome,))
        senha_check = mensager.fetchall()
        

        if (nome,) in nome_check and (senha,) in senha_check : 
            print(f"Bem vindo {nome}")
        else:
            print("Usuário ou senha inválidos")



        

teste = UserManager()
teste.inserir()
teste.login()
