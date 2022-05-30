import sqlite3


banco_db = sqlite3.connect('banco_de_dados.db')
cursor = banco_db.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text,idade integer, email text)")

create_table()


def pedir_dados():
    nome = input("nome>")
    idade = str(input("idade>"))
    email = input("email>")

    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+idade+",'"+email+"')")

    banco_db.commit()#este comando salva os dados no banco de dados


def ver_tabela():
    cursor.execute("SELECT * FROM pessoas")

    ver_db = cursor.fetchall()

    print(ver_db)

print("digite 1 para ver o banco de dados ")
print("digite 2 para inserir dados no banco de dados ")
escolha = int(input(">"))


match escolha:

    case 1:
        ver_tabela()

    case 2:
        pedir_dados()

    case _:
        print("digite penas 1 ou 2")

