from connection import *
from os import system

def pause():
    system("pause >nul")
    system("cls")

def limpar():
    system("cls")

def pesquisar():
    connection = connect_db()
    cursor = connection.cursor()
    result = ""
    sql = "SELECT * FROM telas WHERE modelo="
    values = input("DIGITE O MODELO A PROCURAR A PEÇA: ")
    comando = sql + "'" + values + "'"
    cursor.execute(comando)
    for (id,marca,modelo,cor,quantidade,grau_importancia) in cursor:
        result = result + "\n" + "MARCA: " + marca + "\n" + "MODELO: " + modelo + "\n" + "COR: " + cor + "\n" + "QUANTIDADE: " + str(quantidade) + "\n\n"
    cursor.close()
    connection.commit()
    connection.close()
    return result

def pecas_faltosas():
    connection = connect_db()
    cursor = connection.cursor()
    op = -1
    while (op!=0):
        print("MENU PEÇAS FALTOSAS.\n")
        print("DIGITE O NÚMERO CORRESPONDENTE AO GRAU DE IMPORTÂNCIA:\n")
        print("0-VOLTAR.")
        print("1-GRAU DE IMPORTÂNCIA ALTO.")
        print("2-GRAU DE IMPORTÂNCIA MÉDIO.")
        print("3-GRAU DE IMPORTÂNCIA MÉDIO BAIXO.")
        print("4-GRAU DE IMPORTÂNCIA BAIXO.")
        try:
            op = int(input("\nSUA OPÇÃO: "))
            if (op==0):
                pass
            elif (op==1):
                op="A"
            elif (op==2):
                op="M"
            elif (op==3):
                op="MB"
            elif (op==4):
                op="B"
            else:
                print("\nOPÇÃO INVÁLIDA.")
                pause()
        except ValueError:
            print("\nDIGITE UM NÚMERO VÁLIDO!")
            pause()
            op = -1
    


