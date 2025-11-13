# TERMINAL
# conda create -n p39 python=3.9 pandas numpy scipy matplotlib seaborn
# Windows e MAC
# conda activate p39
# source activate

# A biblioteca certa para trabalhar com dinheiro em python DECIMAL
# Numpy é baseado em C
import random
import numpy as np
import matplotlib.pyplot as plt


def calculate_gini(incomes):
    # Sort smallest to largest
    cumm = np.sort(incomes)
    # Values cannot be 0
    cumm += .00001
    # Find cumulative totals
    n = cumm.shape[0]
    index = np.arange(1, n + 1)
    gini = ((np.sum((2 * index - n - 1) * cumm)) / (n * np.sum(cumm)))
    return gini


def function_to_be_vectorized(x, y):
    if x > y:
        return x - y
    else:
        return x + y


def generate_grid(menor_x, maior_x, menor_y, maior_y, size):
    # Os dois eixos x e y
    x = np.linspace(menor_x, maior_x, size)
    y = np.linspace(menor_y, maior_y, size)
    # O grid com cada coordenada x e y
    xx, yy = np.meshgrid(x, y)
    # A matriz Z que tem um valor para cada combinação de x e y, portanto 101 x 101
    # zz = .4 * xx ** 2 + np.sin(yy) ** 3 + np.cos(xx) * 2.1
    # zz = np.random.random((101, 101)) * np.random.random((101, 101))
    # zz = np.log(np.random.random((101, 101)))
    zz = np.exp(np.random.random((101, 101)))
    print(zz.shape)
    return xx, yy, zz


def plot_countour(xx, yy, zz):
    plt.contourf(xx, yy, zz)
    plt.axis('scaled')
    plt.colorbar()
    plt.show()


if __name__ == '__main__':

    # 1. Create an array
    a = np.arange(10)
    ones = np.ones(10)
    zeros = np.zeros(10)
    diagonal = np.eye(4, 4)

    # Also, passing a list, or a list of lists
    a = np.array([7, 5, 4, 34, 3, 2, 1])
    b = np.array([[4, 3, 6], [7, 6, 0], [90, 1, 117]])

    # 2. Transform into matrix
    a = np.arange(9).reshape(3, 3)

    print(a.size)
    print(a.shape)

    # 3. Operations are ELEMENTWISE. Um por um.
    # Para cálculos de matrizes, utilize outros comandos (np.dot ou np.linalg.inv).
    # Padrão é ELEMENTO POR ELEMENTO.

    c = b ** 2
    c = b * a
    c = b + a
    c = a * 10 - b * a

    # 4. Gotchas! ##### ##### ##### ##### #####
    # Check: https://www.kdnuggets.com/2020/07/numpy-handle-dimensions.html
    # Note a diferença
    d = np.arange(4)
    print(d.shape)

    e = np.arange(4).reshape(4, 1)
    print(e.shape)

    # Preste atenção
    print(d.T.shape)
    print(e.T.shape)

    # 5. Outro ponto relevante é manter somente elementos de mesmo TIPO. dtype. Menos flexível que pandas, por exemplo.

    # 6. Operando por AXIS
    print(b.sum(axis=0))  # Por coluna
    print(b.sum(axis=1))  # Por linha

    # Com 3 dimensões
    b = np.arange(27).reshape((3, 3, 3))
    print(b.ndim)

    # 7. Arrays espaçados, intervalos: incluídos(start, stop), size
    c = np.linspace(0, 1, 100)
    d = np.linspace(2, 3, 5)

    # 8. Várias op44erações com matrizes possíveis. Todas as restrições matemáticas se impõem.
    # Por exemplo: inverso de uma matriz [quadrada].

    m = np.random.randint(1, 10, 4).reshape(2, 2)  # size=100
    print(np.linalg.inv(m))

    nn = np.random.randn(4).reshape(2, 2)
    print(np.linalg.inv(nn))

    # 9. Vectorize a function. Adapted from Numpy: for the beginners, Satyaki Das, p. 193
    new_vectorized_function = np.vectorize(function_to_be_vectorized)

    new_vectorized_function([1, 2, 3, 4], 2)
    new_vectorized_function([1, 2, 3, 4], [1, 2, 3, 4])
    new_vectorized_function(2, [1, 2, 3, 4])

    w = new_vectorized_function(np.random.randint(1, 10, 100000), 5)

    # 10. Conditions. np.where
    # SINTAXE: O JEITO CERTO DE ENTRAR A INFORMAÇÃO:
    # CONDIÇÃO, SE VERDADEIRO, SE FALSO
    w = np.where(a < 5, a, 100)
    w = np.where(a < 5, a, a ** 3)
    w = np.where(a < 5, 0, 1)
    w = np.where(a % 2 != 0, 1, 0)
    w = np.where(a % 2 == 0, 0, 1)

    # 11. Slicing. Just as lists
    a = np.arange(20).reshape(4, 5)
    print(a[0][0])
    print(a[:3])
    print(a[:-1])
    # Dividir com vírgula para o próximo elemento
    print(a[-1, -1])  # último elemento, do último array/lista
    print(a[:-1, -1])  # últimos elementos de até o último array/lista

    # 12, Meshgrid. from docs: Return coordinate matrices from coordinate vectors.
    j, k, o = generate_grid(-5, 5, -5, 5, 101)
    plot_countour(j, k, o)

    # 7. Real-life: calculating GINI coefficient
    mu = 1.7
    salaries = np.random.lognormal(mean=mu, size=1000000)
    print(f'Estimated gini from a lognormal distribution with mean={mu} is {calculate_gini(salaries):.04f}')
