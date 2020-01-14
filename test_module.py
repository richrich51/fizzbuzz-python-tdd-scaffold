import unittest
import fizz_buzz

num = [1, 3, 5, 15]
res = [1, "Fizz", "Buzz", "FizzBuzz"]


class FizzBuzzTest(unittest.TestCase):
    def test_case(self):
        for i in range(len(num)):
            self.assertEqual(res[i], fizz_buzz.get_fizz_buzz(num[i]))


if __name__ == '__main__':
    unittest.main()
