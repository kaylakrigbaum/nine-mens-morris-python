import unittest
from main import *

class testPiecePlacement(unittest.TestCase):
    def test_playing_true(self):
        menu()
        if playing == 1:
            self.assertTrue(playing, "Playing is true, therefore game has started")
        else:
            self.assertFalse(playing, "Playing is not True")

    def test_phase1_init(self):
        menu()
        self.assertTrue(drop_piece(), "Phase 1 has initialized")

    def test_phase2_init(self):
        menu()
        p1 = player()
        p2 = player()
        self.assertEqual(p1.placedPieces, 9, 'Player 1 has placed all nine pieces')
        self.assertEqual(p2.placedPieces, 9, 'Player 2 has placed all nine pieces')

    def test_phase3_init(self):
        menu()
        p1 = player()
        p2 = player()
        self.assertEqual(p1.pieceCount, 3, "Player 1 has reached 3 remaining pieces") or self.assertEqual(p2.pieceCount, 3, "Player 2 has reached 3 remaining pieces")

if __name__ == '__main__':
    unittest.main()
