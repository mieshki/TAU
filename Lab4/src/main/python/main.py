import random
import unittest
from enum import Enum
from items import *

class Player:
    current_width = None
    current_height = None

    def __init__(self, starting_height, starting_width):
        self.current_height = starting_height
        self.current_width = starting_width

    def get_current_position(self):
        return self.current_height, self.current_width

    def set_new_position(self, height, width):
        self.current_height = height
        self.current_width = width


class Direction(Enum):
    UP = 1,
    RIGHT = 2,
    DOWN = 3,
    LEFT = 4


class Game2D:
    def print_board(self):
        for row in self.board:
            for element in row:
                print(f'{element}', end='')
            print('')

    def initialize_borders(self):
        for h in range(self.BOARD_HEIGHT):
            for w in range(self.BOARD_WIDTH):
                if w == 0 or w == self.BOARD_WIDTH - 1 or h == 0 or h == self.BOARD_HEIGHT - 1:
                    self.board[h][w] = self.BORDER_SYMBOL

    def is_move_allowed(self, height, width):
        element = self.board[height][width]
        if element == self.BORDER_SYMBOL:
            return False
        else:
            return True

    def change_player_position(self, height, width, is_first_move=False):
        if self.is_move_allowed(height, width):
            if is_first_move:
                self.board[height][width] = self.PLAYER_SYMBOL
            else:
                previous_height, previous_width = self.player.get_current_position()
                self.board[previous_height][previous_width] = self.EMPTY_SYMBOL
                self.board[height][width] = self.PLAYER_SYMBOL
                self.player.set_new_position(height, width)
            return True
        else:
            return False

    def generate_chest(self, height, width):
        if self.is_move_allowed(height, width) is False:
            print(f'Can\'t generate chest at {height}x{width}')
        else:
            self.board[height][width] = self.CHEST_SYMBOL

    def create_and_insert_player(self, height, width):
        if self.player_created:
            # print(f'Only 1 player allowed!')
            raise Exception('PlayerAlreadyCreated')

        self.player = Player(height, width)
        self.change_player_position(height, width, True)
        self.player_created = True

    def generate_chest_loot(self, rng):
        item_found = False

        if rng == 0:
            self.current_item = Knife()
            item_found = True
        elif rng == 1:
            self.current_item = Glass()
            item_found = True
        elif rng == 2:
            self.current_item = Needle()
            item_found = True
        elif rng == 3:
            self.current_item = Rock()
            item_found = True
        elif rng == 4:
            self.current_item = Water()
            item_found = True
        elif rng == 5:
            self.current_item = Flashlight()
            item_found = True
        elif rng == 6:
            self.current_item = Key()
            item_found = True
        else:
            print('Nothing here')
            self.current_item = None

        if item_found:
            print(f'There was a {self.current_item.describe()}!')

    def move_player(self, direction):
        current_height, current_width = self.player.get_current_position()
        new_height, new_width = 0, 0

        if direction == Direction.UP:
            new_height, new_width = (current_height - 1, current_width)
        elif direction == Direction.RIGHT:
            new_height, new_width = (current_height, current_width + 1)
        elif direction == Direction.DOWN:
            new_height, new_width = (current_height + 1, current_width)
        elif direction == Direction.LEFT:
            new_height, new_width = (current_height, current_width - 1)

        if self.board[new_height][new_width] == self.CHEST_SYMBOL:
            print(f'Found chest!')
            self.chest_collected = True
            self.generate_chest_loot(random.randint(0, 8))

        result = self.change_player_position(new_height, new_width)
        if result is False:
            print(f'Move {direction} not allowed')
            return False
        else:
            return True

    def __init__(self, player_starting_height=4, player_starting_width=4):
        self.BOARD_WIDTH = 20
        self.BOARD_HEIGHT = 10
        self.BORDER_SYMBOL = '#'
        self.EMPTY_SYMBOL = ' '
        self.CHEST_SYMBOL = 'C'
        self.PLAYER_SYMBOL = 'P'
        self.player_created = False
        self.player = None
        self.current_item = None
        self.chest_collected = False
        self.board = [[self.EMPTY_SYMBOL] * self.BOARD_WIDTH for i in range(self.BOARD_HEIGHT)]

        self.initialize_borders()
        self.create_and_insert_player(player_starting_height, player_starting_width)


if __name__ == '__main__':
    game = Game2D()
    game.generate_chest(6, 4)

    for i in range(4):
        game.print_board()
        game.move_player(Direction.DOWN)