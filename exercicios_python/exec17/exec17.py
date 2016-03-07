flag = True

while flag:
    name = input("Forneça o nome:")
    password = input("Forneça a senha:")
    if name != password:
        flag = False
        continue
    print("Erro. Nome e senha são iguais.")
