def show_impar():
    for item in range(100,200):
        if item % 2 == 0:
            continue
        print("O numero %d é impar" % item)

show_impar()
