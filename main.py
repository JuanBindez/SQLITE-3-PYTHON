'''
Author: www.github.com/JuanBindez
Description: Connection Sqlite3
Python Version: 3.10
year: 2022
Local: Brazil
'''


import sqlite3
import os


banco_db = sqlite3.connect("banco_de_dados.db")
cursor = banco_db.cursor()

def linha():
    print("=======================================================")


def criar_banco():
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, idade integer, email text)")

criar_banco()


def pedir_dados():
    nome = input("nome>")
    idade = str(input("idade>"))
    email = input("email>")

    cursor.execute("INSERT INTO cadastro VALUES('"+nome+"',"+idade+",'"+email+"')")

    banco_db.commit()#este comando salva os dados no banco de dados
    os.system("clear")
    linha()
    menu()


def ver_banco():
    cursor.execute("SELECT * FROM cadastro")

    ver_db = cursor.fetchall()
    os.system("clear")
    linha()
    print("  nome  idade     email")

    for pessoa in ver_db:
        print(pessoa)

    linha()
    menu()


def menu():
    print(
        '''
                            SQLITE 3 COM PYTHON

                        [1] para ver o banco de dados
                        [2] para inserir dados no banco de dados 
        '''
    )

    
    escolha = int(input(">"))


    match escolha:

        case 1:
            ver_banco()

        case 2:
            pedir_dados()

        case _:
            print("digite apenas 1 ou 2")

os.system("clear")
menu()
