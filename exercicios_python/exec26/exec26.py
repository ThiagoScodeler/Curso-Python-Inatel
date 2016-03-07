def calc_vet():
    vet_numbers = list()
    for n in range(4):
        vet_numbers.append(int(input("Forneça um número: ")))

    vet_par = list((n for n in vet_numbers if n % 2 == 0))
    vet_impar = list((n for n in vet_numbers if n % 2 != 0))

    print("Lista original: ")
    print(vet_numbers)
    print("Lista par: ")
    print(vet_par)
    print("Lista ímpar: ")
    print(vet_impar)

if __name__ == '__main__':
    calc_vet()
