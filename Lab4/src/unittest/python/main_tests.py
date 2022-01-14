import mock
import verify
import unittest
from main import Game2D, Direction
from items import *

class GameTest(unittest.TestCase):
    def test_player_move_up_allowed(self):
        starting_height, starting_width = 2, 2
        game = Game2D(starting_height, starting_width)
        game.move_player(Direction.UP)
        self.assertTrue(game.player.get_current_position() == (starting_height - 1, starting_width))
        self.assertEqual(game.board[starting_height][starting_width], ' ', 'Player still exists at previous location!')
        self.assertEqual(game.board[starting_height - 1][starting_width], 'P')

    def test_player_move_up_not_allowed(self):
        starting_height, starting_width = 1, 2
        game = Game2D(starting_height, starting_width)
        self.assertFalse(game.move_player(Direction.UP))

    def test_player_move_right_allowed(self):
        starting_height, starting_width = 2, 2
        game = Game2D(starting_height, starting_width)
        game.move_player(Direction.RIGHT)
        self.assertTrue(game.player.get_current_position() == (starting_height, starting_width + 1))

    def test_player_move_right_not_allowed(self):
        starting_height, starting_width = 1, 18
        game = Game2D(starting_height, starting_width)
        self.assertFalse(game.move_player(Direction.RIGHT))

    def test_player_move_down_allowed(self):
        starting_height, starting_width = 2, 2
        game = Game2D(starting_height, starting_width)
        game.move_player(Direction.DOWN)
        self.assertTrue(game.player.get_current_position() == (starting_height + 1, starting_width))

    def test_player_move_down_not_allowed(self):
        starting_height, starting_width = 8, 2
        game = Game2D(starting_height, starting_width)
        self.assertFalse(game.move_player(Direction.DOWN))

    def test_player_move_left_allowed(self):
        starting_height, starting_width = 2, 2
        game = Game2D(starting_height, starting_width)
        game.move_player(Direction.LEFT)
        self.assertTrue(game.player.get_current_position() == (starting_height, starting_width - 1))

    def test_player_move_left_not_allowed(self):
        starting_height, starting_width = 1, 1
        game = Game2D(starting_height, starting_width)
        self.assertFalse(game.move_player(Direction.LEFT))

    def test_generate_chess_allowed(self):
        game = Game2D(2, 2)
        game.generate_chest(5, 5)

    def test_check_player_creation_duplicate(self):
        game = Game2D(2, 2)
        with self.assertRaises(Exception) as context:
            game.create_and_insert_player(2, 2)
            self.assertTrue('PlayerAlreadyCreated' in context.exception)

    def test_find_chest(self):
        game = Game2D()
        game.generate_chest(6, 4)

        for i in range(4):
            game.print_board()
            game.move_player(Direction.DOWN)

        verify.is_true(game.chest_collected)

    def test_generate_knife(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(0)
        verify.matches('Knife', game.current_item.describe())

    def test_generate_glass(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(1)
        verify.matches('Glass', game.current_item.describe())

    def test_generate_needle(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(2)
        verify.matches('Needle', game.current_item.describe())

    def test_generate_rock(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(3)
        verify.matches('Rock', game.current_item.describe())

    def test_generate_water(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(4)
        verify.matches('Water', game.current_item.describe())

    def test_generate_flashlight(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(5)
        verify.matches('Flashlight', game.current_item.describe())

    def test_generate_key(self):
        game = Game2D(2, 2)
        game.generate_chest_loot(6)
        verify.matches('Key', game.current_item.describe())

    def test_generate_nothing(self):
        game = Game2D(2, 2)

        game.generate_chest_loot(7)
        game.generate_chest_loot(8)

        verify.is_true(game.current_item is None)