import unittest
import fizz_buzz

fb = dict()
fb[1] = 1
fb[3] = "Fizz"
fb[5] = "Buzz"
fb[15] = "FizzBuzz"


class TestFizzBuzz(unittest.TestCase):
    def test_case(self):
        for k, v in fb.items():
            self.assertEqual(v, fizz_buzz.get_fizz_buzz(k))


if __name__ == '__main__':
    unittest.main()
