from connection import *

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
    


