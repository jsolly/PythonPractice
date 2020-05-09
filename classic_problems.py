

def fizz_buzz(num):
    if num == 0:
        return 0

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    elif num % 3 == 0:
        return "Fizz"

    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def fibonacci(num):
    a, b = 0, 1

    for i in range(0, num):
        print(a)
        a, b = b, a+b


def fibonacci_generator(num):
    a, b = 0, 1

    for i in range(0, num):
        yield a
        a, b = b, a + b
