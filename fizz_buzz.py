def get_fizz_buzz(n):
    ext = 10 * (n % 5) + n % 3

    if ext != 0:
        if ext % 10 == 0:
            return "Fizz"
        elif ext < 3:
            return "Buzz"
        return n
    else:
        return "FizzBuzz"
