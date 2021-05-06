# unit tests with unittest

import unittest
import driver


class MyTestCase(unittest.TestCase):

    def test_translate_zero(self):
        result = driver.translate(0)
        self.assertEqual(result, 0)

    def test_translate_twelve(self):
        result = driver.translate(12)
        self.assertEqual(result, 12)

    def test_translate_red(self):
        result = driver.translate('red')
        self.assertEqual(result, 13)

    def test_translate_black(self):
        result = driver.translate('black')
        self.assertEqual(result, 14)

    def test_translate_odd(self):
        result = driver.translate('odd')
        self.assertEqual(result, 15)

    def test_translate_even(self):
        result = driver.translate('even')
        self.assertEqual(result, 16)

    def test_translate_high(self):
        result = driver.translate('high')
        self.assertEqual(result, 17)

    def test_translate_low(self):
        result = driver.translate('low')
        self.assertEqual(result, 18)

    def test_translate_row1(self):
        result = driver.translate('row1')
        self.assertEqual(result, 19)

    def test_translate_row2(self):
        result = driver.translate('row2')
        self.assertEqual(result, 20)

    def test_translate_row3(self):
        result = driver.translate('row3')
        self.assertEqual(result, 21)

    def test_reverse_translate_zero(self):
        result = driver.reverse_translate(0)
        self.assertEqual(result, 0)

    def test_reverse_translate_twelve(self):
        result = driver.reverse_translate(12)
        self.assertEqual(result, 12)

    def test_reverse_translate_red(self):
        result = driver.reverse_translate(13)
        self.assertEqual(result, 'red')

    def test_reverse_translate_black(self):
        result = driver.reverse_translate(14)
        self.assertEqual(result, 'black')

    def test_reverse_translate_odd(self):
        result = driver.reverse_translate(15)
        self.assertEqual(result, 'odd')

    def test_reverse_translate_even(self):
        result = driver.reverse_translate(16)
        self.assertEqual(result, 'even')

    def test_reverse_translate_high(self):
        result = driver.reverse_translate(17)
        self.assertEqual(result, 'high')

    def test_reverse_translate_low(self):
        result = driver.reverse_translate(18)
        self.assertEqual(result, 'low')

    def test_reverse_translate_row1(self):
        result = driver.reverse_translate(19)
        self.assertEqual(result, 'row1')

    def test_reverse_translate_row2(self):
        result = driver.reverse_translate(20)
        self.assertEqual(result, 'row2')

    def test_reverse_translate_row3(self):
        result = driver.reverse_translate(21)
        self.assertEqual(result, 'row3')

    def test_win_checker_zero(self):
        result = driver.win_checker(0,
                                    [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [1200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_win_checker_one(self):
        result = driver.win_checker(1,
                                    [1, 200, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 2400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 32, 0, 0, 38, 60, 0, 0])

    def test_win_checker_two(self):
        result = driver.win_checker(2,
                                    [1, 2, 300, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 3600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 34, 0, 38, 0, 63, 0])

    def test_win_checker_three(self):
        result = driver.win_checker(3,
                                    [1, 2, 3, 400, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 4800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 28, 0, 32, 0, 0, 38, 0, 0, 66])

    def test_win_checker_four(self):
        result = driver.win_checker(4,
                                    [1, 2, 3, 4, 500, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 6000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 34, 0, 38, 60, 0, 0])

    def test_win_checker_five(self):
        result = driver.win_checker(5,
                                    [1, 2, 3, 4, 5, 600, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 7200, 0, 0, 0, 0, 0, 0, 0, 28, 0, 32, 0, 0, 38, 0, 63, 0])

    def test_win_checker_six(self):
        result = driver.win_checker(6,
                                    [1, 2, 3, 4, 5, 6, 700, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 8400, 0, 0, 0, 0, 0, 0, 0, 30, 0, 34, 0, 38, 0, 0, 66])

    def test_win_checker_seven(self):
        result = driver.win_checker(7,
                                    [1, 2, 3, 4, 5, 6, 7, 800, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 9600, 0, 0, 0, 0, 0, 0, 30, 32, 0, 36, 0, 60, 0, 0])

    def test_win_checker_eight(self):
        result = driver.win_checker(8,
                                    [1, 2, 3, 4, 5, 6, 7, 8, 900, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 10800, 0, 0, 0, 0, 28, 0, 0, 34, 36, 0, 0, 63, 0])

    def test_win_checker_nine(self):
        result = driver.win_checker(9,
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0, 12000, 0, 0, 0, 0, 30, 32, 0, 36, 0, 0, 0, 66])

    def test_win_checker_ten(self):
        result = driver.win_checker(10,
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1100, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13200, 0, 0, 28, 0, 0, 34, 36, 0, 60, 0, 0])

    def test_win_checker_eleven(self):
        result = driver.win_checker(11,
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1200, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14400, 0, 0, 30, 32, 0, 36, 0, 0, 63, 0])

    def test_win_checker_twelve(self):
        result = driver.win_checker(12,
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1300, 14, 15, 16, 17, 18, 19, 20, 21, 22])
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15600, 28, 0, 0, 34, 36, 0, 0, 0, 66])

if __name__ == '__main__':
    unittest.main()
