def init(tpl_1, tpl_2):
    new_tupla = tpl_1 + tpl_2;
    return new_tupla

if __name__ == '__main__':
    tupla_1 = (14, 2, 5, 9, 0)
    tupla_2 = (4, 9, 3, 1, 7)
    new_tupla = init(tupla_1,tupla_2)
    print(new_tupla)
