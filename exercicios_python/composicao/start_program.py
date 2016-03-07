from entidades import Player
from entidades import Enemy
from entidades import Game

def main():

    player = Player()
    enemy = Enemy()
    game = Game(player,enemy)
    game.run_player()
    game.run_enemy()

if __name__ == '__main__':
    main()
