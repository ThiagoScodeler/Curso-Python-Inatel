class Food(object):

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def tastesLike(self):
        raise NotImplementedException('Subclasses are responsible for creating this method')


class HotDog(Food):

    def tastesLike(self):
        return 'Extremely processed meat'


class Hamburguer(Food):

    def tastesLike(self):
        return 'grilled goodness'


class ChickenPatty(Food):

    def tastesLike(self):
        return 'tastes like chicken'
