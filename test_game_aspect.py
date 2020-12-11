import unittest
from main import *

class TestGameAspects(unittest.TestCase):
    def test_player_vs_player_button(self):
        if menu() == 1:
            self.assertEqual(menu(), 1, "User Selected Player vs Player Successfully")
        else:
            self.assertNotEqual(menu(), 1, "User Did not select Player vs Player")

    def test_player_vs_AI_button(self):
        menu()
        if menu() == 2:
            self.assertEqual(menu(), 2, "User Selected Play vs AI Successfully")
        else:
            self.assertNotEqual(menu(), 2, "User did not select play vs AI ")

    def test_player_quit_button(self):
        menu()
        if menu() == 0:
            self.assertEqual(menu(), 0, "User Selected the Quit button")
        else:
            self.assertNotEqual(menu(), 0, "User did not select Quit")

if __name__ == '__main__':
    unittest.main()
