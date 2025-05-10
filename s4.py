import unittest

from s2 import f5, f4


class TestFunctions(unittest.TestCase):
    def test_f4(self):
        self.assertEqual(f4([1, 2, 3, 4]), "Среднее чётных больше")
        self.assertEqual(f4([1, 3, 5, 7]), "Среднее нечётных больше")
        self.assertEqual(f4([2, 4, 3, 5]), "Средние равны")

    def test_f5(self):
        with self.assertRaises(IndexError):
            f5()  # Тест обнаружит ошибку выхода за границы списка


if __name__ == '__main__':
    unittest.main()