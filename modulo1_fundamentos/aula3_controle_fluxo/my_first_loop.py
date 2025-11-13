for i in 'hello world':
    print(i)

for i in 'hello world':
    print(i.capitalize())

for num in range(10):
    print(num)

for i in range(len('hello')):   #  é a mesma coisa range(5)
    print(i)

for each in ['apples', 'bananas', 'peaches']:
    print(each)


for each in ['maria', 'joana', 'joaquim']:
    print(each.capitalize())

for each in ['maria', 'joana', 'joaquim']:
    print(each.capitalize(), end=' ')


for each in ['maria', 'joana', 'joaquim']:
    print(each.capitalize())
#
print('maria', 'joana', 'joaquim')
print('maria', 'joana', 'joaquim', sep=' ** ')

for each in range(10):
    print(f'{each} vezes {each} é {each ** 2}')

def taboada():
    print('Tentativa de uma taboada')
    for i in range(5, 10):
        print('________________')
        for j in range(5, 10):
            print(f'{i} vezes {j} é {i * j}')


for i in range(-10, 1):
    print(i)
#
# for i in range(1, 11, 2):
#     print(i)
#
for word in "The quick brown fox jumps over the lazy dog".split():
    print(word.title())
#
for word in "The quick brown fox \njumps over\nthe lazy dog".split(sep='\n'):
    print(word.title())


if __name__ == '__main__':
    taboada()


