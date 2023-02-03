from functions import *

menu_principal = -1
while (menu_principal != 0):
    limpar()
    print("MENU PRINCIPAL.\n")
    print("0-SAIR")
    print("1-PESQUISAR.")
    print("2-PEÇAS FALTOSAS.")
    print("3-MOSTRAR ESTOQUE.\n")
    try:
        menu_principal = int(input("SUA OPÇÃO: "))
        if (menu_principal==1):
            limpar()
            pesquisa = pesquisar()
            print(pesquisa)
            pause()
        elif (menu_principal==2):
            limpar()
            pecas_faltosas()
        elif (menu_principal==3):
            limpar()
            mostrar_estoque()
            pause()
    except ValueError:
        print("\nDIGITE UM NÚMERO VÁLIDO!")
        pause()