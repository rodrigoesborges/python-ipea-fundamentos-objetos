""" Transforme o código abaixo em uma função que receba dois parâmetros e retorne a soma deles.
Além disso, adicione tratamento de exceção para garantir que os valores inseridos sejam números. 
Dica 1: use try/except para capturar ValueError ao converter a entrada para float.
Somente retorne a soma se ambos os valores forem válidos.
Insista para que o usuário insira números válidos caso ele cometa um erro."""

# Dica 2: use um loop while para continuar pedindo a entrada até que valores válidos sejam fornecidos.
# Dica 3: use lista == len(2) para sair do loop quando valores válidos forem obtidos.
# Dica 4: use len() para verificar a quantidade de valores a serem somados.


try:
    x = float(input('Entre um número: '))
except ValueError:
    print('Você não entrou um número... Por favorzinho, entre com um número inteiro')
    x = float(input('Entre um número: '))


# f-string
# python 3.6 para cá.
# texto corrido + variáveis
# print(f"Este é um texto de exemplo para a variável x {x}")



