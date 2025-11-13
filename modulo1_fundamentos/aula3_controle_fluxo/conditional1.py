""" Learning about conditionals
    Pay attention to the COLON after the condition
    Note else is different from elif
    """


def is_positive(x):
    # esta é uma função...
    if x > 0:
        print(f'{x} é positivo')
    elif x < 0:
        print(f'{x} é negativo')
    else:
        print('é nulo')


def determine_input(x):
    if type(x) == str:
        print(f'{x} é uma string')
        t_str(x)
    else:
        print(f'{x} provavelmente é um número ')
        t_valor(x)


def t_valor(x):
    if x > 0:
        print('x is positive')
    elif x == 0:
        print('x is zero')
    else:
        print('x is negative')


def t_str(x):
    if x in 'aeiou':
        print(f'{x} is a vowel')
    elif x == 'z':
        print(f'{x} is z')
    elif x in 'AEIOU':
        print(f'{x} is a capital vowel')
    else:
        print(f'Não tenho idea do que é {x}')


if __name__ == '__main__':
    a = is_positive(-10)
    y = 20
    determine_input(y)
    y = 'o'
    determine_input(y)
