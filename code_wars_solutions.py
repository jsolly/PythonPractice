import string


def is_pangram(s):
    s = s.lower()
    alphabet = string.ascii_lowercase

    if len(set(alphabet).intersection(s)) == 26:
        return True

    return False


def valid_parentheses(s):
    if not s:
        return True
    elif s.count("(") != s.count(")"):
        return False

    parentheses_string = "".join([character for character in s if character in "()"])
    while True:
        parentheses_string = parentheses_string.replace("()", "")
        if parentheses_string == ")(":
            return False
        if parentheses_string == "":
            return True


def solution(s):
    if not s:
        return []

    split_string = [(s[index : index + 2]) for index in range(0, len(s), 2)]

    if len(split_string[-1]) == 1:
        split_string[-1] += "_"
    return split_string


def make_readable(seconds):
    whole_hours = seconds // 3600 if seconds >= 3600 else 0
    remainder_seconds = seconds % 3600
    whole_minutes = remainder_seconds // 60 if 0 < remainder_seconds < 3600 else 0
    whole_seconds = remainder_seconds % 60

    return f"{whole_hours:02}:{whole_minutes:02}:{whole_seconds:02}"


def create_phone_number(numbers: list):
    number_string = "".join(str(digit) for digit in numbers)

    return f"({number_string[:3]}) {number_string[3:6]}-{number_string[6:10]}"


def comp(array1, array2):
    if not array1 and not array2:
        return False

    a_squared = [pow(number, 2) for number in array1]
    if set(a_squared) == set(array2):
        return True
    return False


def decode_morse(code):
    morse_code_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "--..--": ", ",
        ".-.-.-": ".",
        "..--..": "?",
        "-..-.": "/",
        "-....-": "-",
        "-.--.": "(",
        "-.--.-": ")",
    }

    translated_message = " ".join(
        [
            "".join(
                [morse_code_dict[morse_letter] for morse_letter in morse_word.split()]
            )
            for morse_word in code.split("   ")
        ]
    )

    return translated_message.strip()


def find_outlier(integers: list):
    def check_int_type(integer, int_type):
        remainder = integer % 2
        if remainder == 1 and int_type == "even":
            return False

        elif remainder == 0 and int_type == "odd":
            return False

        else:
            return True

    even_count = 0
    current_type = "even"
    for i in integers[:3]:
        if check_int_type(i, current_type):
            even_count += 1

    current_type = current_type if even_count >= 2 else "odd"

    for number in integers:
        if not check_int_type(number, current_type):
            return number


def song_decoder(song: str):
    removed_wubs = [word for word in song.split("WUB") if word != "WUB"]
    while "" in removed_wubs:
        removed_wubs.remove("")
    final_string = " ".join(removed_wubs)
    return final_string


def digital_root_sum(n):
    while n > 10:
        n = sum((int(n) for n in str(n)))
    return n


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
