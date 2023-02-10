def connect_db():
    from os import system
    import mysql.connector
    from mysql.connector import errorcode

    try:
        db_connection = mysql.connector.connect(host='localhost',user='root',port='3300',password='Campodomeio1',database='estoque')
        print("Conexão com banco de dados foi feita!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe!")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuário e ou senha está incorreto, ou o Banco de dados está offline!")
        else: 
            print(error)
    system("pause >nul")
    system("cls")
    return db_connection

