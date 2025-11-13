import calculos_main


def imprime_lista(dados):
    print("Lista de dados:")
    for numero in dados:
        print(numero)


def main():
    dados = calculos_main.cria_lista(100)
    imprime_lista(dados)


if __name__ == '__main__':
    main()
    