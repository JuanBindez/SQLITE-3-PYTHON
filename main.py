'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
'''


'''
Author: www.github.com/JuanBindez
Description: Connection Sqlite3
Python Version: 3.10
year: 2022
Local: Brazil
'''


import sqlite3
import os

try:
    banco_db = sqlite3.connect("banco_de_dados.db")
    cursor = banco_db.cursor()

    def linha():
        print("=======================================================")


    def criar_banco():
        cursor.execute("CREATE TABLE IF NOT EXISTS cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, email TEXT)")

    criar_banco()


    def pedir_dados():
        nome = input("nome>")
        idade = str(input("idade>"))
        email = input("email>")

        cursor.execute("INSERT INTO cadastro VALUES(NULL,'"+nome+"',"+idade+",'"+email+"')")

        banco_db.commit()#este comando salva os dados no banco de dados
        os.system("clear")
        linha()
        menu()


    def ver_banco():
        cursor.execute("SELECT * FROM cadastro")

        ver_db = cursor.fetchall()
        os.system("clear")
        linha()
        print(" id  nome  idade        email")

        for pessoa in ver_db:
            print(pessoa)

        linha()
        menu()

    def deleta_id(i):
            query = "DELETE FROM cadastro WHERE id=?"
            cursor.execute(query, i)
            banco_db.commit()


    def menu():
        print(
            '''
                                SQLITE 3 COM PYTHON
                            [1] para ver o banco de dados
                            [2] para inserir dados no banco
                            [3] para deletar id no banco
            '''
        )
        
        escolha = int(input(">"))

        match escolha:

            case 1:
                ver_banco()

            case 2:
                pedir_dados()

            case 3:
                delid = str(input('digite o id a ser deletado'))
                deleta_id(delid)

            case _:
                print("digite apenas os números listados")
                

    os.system("clear")
    menu()
except KeyboardInterrupt:
    os.system("clear")
    print('Você Encerrou o Programa')
