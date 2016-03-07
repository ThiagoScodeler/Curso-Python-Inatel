def main():
    user_chars = list()
    for x in range(10):
        user_chars.append(input('Forneça um caracter: '))

    print("Total de consoantes: ")
    print(sum(1 for item in user_chars if item not in 'aeiou'))

if __name__ == '__main__':
    main()
