import unittest
from main import Game2D, Direction


class TestGame2D(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()