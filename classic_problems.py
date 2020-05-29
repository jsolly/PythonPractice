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
        a, b = b, a + b


# Generator examples
def fibonacci_generator(num):
    a, b = 0, 1

    for i in range(0, num):
        yield a
        a, b = b, a + b


def sentence_gen_func(sentence):
    for word in sentence.split():
        yield word


class Sentence1:
    def __init__(self, sentence):
        self.sentence_iterator = iter(sentence.split())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.sentence_iterator)


class Sentence2:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current_index = self.index
        self.index += 1
        return self.words[current_index]
