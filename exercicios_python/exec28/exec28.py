def main():
    tamanho_agenda = eval(input("Digite o tamanho da agenda: "))
    dict_contatos = {}

    for lista in range(tamanho_agenda):
        name = input("Digite o nome do contato: ")
        idade = eval((input("Digite a idade: ")))
        dict_contatos[name] = idade

    print(dict_contatos)

if __name__ == '__main__':
    main()
