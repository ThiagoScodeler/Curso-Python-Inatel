def result(avg_result):
    if avg_result == 10:
        print("Aprovado com Distinção. Sua nota é: %d" % avg_result)
    elif avg_result >=7:
        print("Aprovado. Sua nota é: %d" % avg_result)
    else:
        print("Reprovado. Sua nota é: %d" % avg_result)

def average(value_1,value_2):
    avg = (value_1+value_2)/2
    result(avg)

def init():
    nota_1 = eval(input("Forneça a primeira nota:"))
    nota_2 = eval(input("Forneça a segunda nota:"))
    average(nota_1,nota_2)

if __name__ == '__main__':
    init()
