from entidades import HotDog, Hamburguer, ChickenPatty

def main():

    dinner = []
    dinner.append(HotDog('Cachorro Quente',230))
    dinner.append(Hamburguer('Carne Mioca',200))
    dinner.append(ChickenPatty('Empadinha',187))

    for food in dinner:
        print(food.name)
        print(food.tastesLike())
        print(' ------ ')


if __name__ == '__main__':
    main()
