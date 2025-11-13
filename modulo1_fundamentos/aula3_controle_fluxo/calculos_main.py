# calculos.py - Este é um módulo com funções de cálculo
import random
import calculos_teste


def cria_lista(n=10):
    dados = list()
    for i in range(n):
        dados.append(random.randint(1, 100))
    return dados


def main():
    """Processa dados e retorna estatísticas"""
    dados = cria_lista()
    media = calculos_teste.calcular_media(dados)
    maior = calculos_teste.encontrar_maior_numero(dados)
    
    resultado = {
        'media': media,
        'maior_numero': maior,
        'quantidade': len(dados)
    }
    print(f'Análise lista aleatória: {resultado}')


if __name__ == '__main__':
    main()

