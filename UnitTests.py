import unittest
import main

class TestGameAspects(unittest.TestCase):
    def test_playing_true(self):
        self.assertEqual(main.playing, True)

    def test_phase1_initiated(self):
        self.assertTrue(main.drop_piece(), True)

    def test_phase2_initiated(self):
        self.assertEqual(main.p1.placedPieces, 9, 'Player 1 has placed all nine pieces')
        self.assertEqual(main.p2.placedPieces, 9, 'Player 2 has placed all nine pieces')

    def test_phase3_initiated(self):
        self.assertEqual((main.p1.pieceCount, 3, 'Player 1 has reached 3 remaining pieces') or self.assertEqual(main.p2.pieceCount, 3, 'Player 2 has reached 3 remaining pieces'))


def mainTwo():
    unittest.main()
if __name__ == '__main__':
    mainTwo()
