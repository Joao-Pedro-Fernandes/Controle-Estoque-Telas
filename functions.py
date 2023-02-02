from connection import *
from os import system

def pause():
    print("\n\n")
    system("pause")
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
    for (id,marca,modelo,cor,grau_importancia,quantidade) in cursor:
        result = result + "\n" + "MARCA: " + marca + "\n" + "MODELO: " + modelo + "\n" + "COR: " + cor + "\n" + "GRAU DE IMPORTÂNCIA: " + grau_importancia + "\n" + "QUANTIDADE: " + str(quantidade) + "\n\n"
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
                break
            elif (op==1):
                sql = "select * from telas where numero_de_pecas='0' and grau_de_importancia='A'"
                cursor.execute(sql)
                for (id,marca,modelo,cor,grau_importancia,quantidade) in cursor:
                    lista = "Frontal" + " " + marca + " " + modelo + " " + cor
                    print(lista)
            elif (op==2):
                sql = "select * from telas where numero_de_pecas='0' and grau_de_importancia='A' or numero_de_pecas='0' and grau_de_importancia='M'"
                cursor.execute(sql)
                for (id,marca,modelo,cor,grau_importancia,quantidade) in cursor:
                    lista = "Frontal" + " " + marca + " " + modelo + " " + cor
                    print(lista)
            elif (op==3):
                op="MB"
                sql = "select * from telas where numero_de_pecas='0' and grau_de_importancia='A' or numero_de_pecas='0' and grau_de_importancia='M' or numero_de_pecas='0' and grau_de_importancia='MB'"
                cursor.execute(sql)
                for (id,marca,modelo,cor,grau_importancia,quantidade) in cursor:
                    lista = "Frontal" + " " + marca + " " + modelo + " " + cor
                    print(lista)                   
            elif (op==4):
                op="B"
                sql = "select * from telas where numero_de_pecas='0' and grau_de_importancia='A' or numero_de_pecas='0' and grau_de_importancia='M' or numero_de_pecas='0' and grau_de_importancia='MB' or numero_de_pecas='0' and grau_de_importancia='B'"
                cursor.execute(sql)
                for (id,marca,modelo,cor,grau_importancia,quantidade) in cursor:
                    lista = "Frontal" + " " + marca + " " + modelo + " " + cor
                    print(lista)
            else:
                print("\nOPÇÃO INVÁLIDA.")
                pause()
            pause()
        except ValueError:
            print("\nDIGITE UM NÚMERO VÁLIDO!")
            pause()
            op = -1
    


