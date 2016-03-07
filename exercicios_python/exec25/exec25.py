def invert_list():
    altura = []
    idade = []

    for i in range(5):
        altura.append(input('Forneça a altura: '))
        idade.append(input("Forneça a idade: "))

    print("Antes ...")
    print(altura)
    print(idade)

    altura.reverse()
    idade.reverse()
    print('Depois ...')
    print(altura)
    print(idade)

if __name__ == '__main__':
    invert_list()
