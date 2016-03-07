class Player(object):

    def run_player(self):
        print('Player running...')


class Enemy(object):

    def run_enemy(self):
        print('Enemy running...')


class Game(object):

    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy

    def run_player(self):
        self.player.run_player()

    def run_enemy(self):
        self.enemy.run_enemy()
