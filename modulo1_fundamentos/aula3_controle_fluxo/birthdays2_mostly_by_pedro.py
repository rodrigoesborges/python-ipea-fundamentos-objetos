import numpy as np
import matplotlib.pyplot as plt


def create_birthdays(students: int) -> list:
    # Use random.randint to create a list of birthdays
    return list(np.random.randint(1, 366, size=students))


def duplicados(birthdays: list) -> bool:
    # Verifique se a lista tem duplicados
    # Lembre-se a função set() retorna um objeto sem duplicados
    return not len(birthdays) == len(set(birthdays))


def simulations(number_simulations: int, number_students: int) -> float:
    # Chame a função create_birthdays e duplicados repetidanente (number) e calcule a probabilidade
    out = list()
    for i in range(number_simulations):
        out += [duplicados(create_birthdays(number_students))]
    # print(f'Probability of having two birthdays on the same day is {sum(out)/len(out):.6f}')
    return sum(out)/len(out)


def main(n_sim):
    ys = list()
    for i in range(1, 100):
        ys.append(simulations(n_sim, i))
    plt.plot(range(1, 100), ys)
    plt.xlabel('Número alunos na classe')
    plt.ylabel('Probability of having two birthdays on the same day')
    plt.show()


if __name__ == '__main__':
    n_simulation = 100
    n_students = 67

    # simulations(n_simulation, n_students)
    main(n_simulation)

