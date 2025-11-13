import random


def generate(n=10):

    l = list()
    for i in range(n):
        l.append(random.randint(0, 10))

    return l


if __name__ == '__main__':

    a = generate()
    print(a)
    print(a.pop())
    print(a.pop())
    #
    print(a)
    #
    for i in range(len(a)):
        print(f'i = {i}')
        print(a[i])
        print(f'O i é {i} e o a[i] é {a[i]}')

    b = generate(5)
    print(b)