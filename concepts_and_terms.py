"""
Idempotence
f(f(x)) = f(x)

Whenever you do something over and over again, you get the same result.

GET
PUT
POST
DELETE

Are always Idempotent

POST is NOT Idempotent (The response can change on multiple tries)
"""
#
# print(abs(abs(-10)))  # Will always be 10
#
"""
Closures

"A closure is an inner function that remembers and has access to variables in
the local scope in which it was created.
"""
#
#
# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# outer_func()
#
"""
Memoization: storing the result of a function so it does not need to be re-run
if the same inputs are seen again.
"""
# import time
#
# ef_cache = {}
#
#
# def expensive_func(num):
#     if num in ef_cache:
#         return ef_cache[num]
#
#     print(f"Computing {num}")
#     time.sleep(1)
#     result = num * num
#     ef_cache[num] = result
#     return num * num
#
#
# result = expensive_func(4)
# print(result)
#
# result = expensive_func(10)
# print(result)
#
# result = expensive_func(4)
# print(result)
#
# result = expensive_func(10)
# print(result)
#
"""
Ternary Conditional
"""
# # condition = False
# # x = 1 if condition else 0
#
"""
formatting large numbers.
2_000_000 # Adding underscores does not affect numbers in Python!
"""
# num1 = 10_000_000_000
# num2 = 100_000_000
# total = num1 + num2
#
# print(f"{total:,}")
#
"""
iterate over two lists at once!
"""
# names = [""]
#
#
# def fibonacci_generator(num):
#     a, b = 0, 1
#     for i in range(0, num):
#         yield a
#         a, b = b, a + b
#
#
# fib_gen = fibonacci_generator(10)
#
#
# def test_fibonacci_generator(fib_gen):
#     first_ten = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     for fib, num in zip(fib_gen, first_ten):
#         assert fib == num
#
#
"""
Tuple unpacking
"""
# # set 'a' and 'b' to 1, 2 and c to everything up to the last one [3, 4] d to 5
# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a, b, c, d)
# # Ignore the rest of the arguments completely
# a, b, *_ = (1, 2, 3, 4, 5)
# print(a, b, c, d)
#
"""
Being 'Pythonic'... EAFP (Easier to ask forgiveness than permission)
'Let's try to do something and if it doesn't work, we will handle it.
vs
Look before you leap (LBYL)
'ask permission every step you take.'

Python can be a lot faster in situations where you don't expect a lot of errors
because you don't have to keep accessing the object to ask it questions before
proceeding.
"""
#
#
# class Person:
#     def quack(self):
#         print("Quack, quack!")
#
#     def walk(self):
#         print("Waddle, Waddle!")
#
#
# class Duck:
#     def quack(self):
#         print("Quack, quack!")
#
#     def walk(self):
#         print("Waddle, Waddle!")
#
#
# # Pythonic
# def is_a_duck_pythonic(thing):
#     try:
#         thing.quack()
#         thing.walk()
#         print("I think this is a Duck!")
#     except AttributeError as e:
#         print(e)
#         print("I don't think this is a duck!")
#
#
# # Non-Pythonic
# def is_a_duck(thing):
#     if hasattr(thing, "quack"):
#         if callable(thing.quack):
#             thing.quack()
#
#         if hasattr(thing, "walk"):
#             if callable(thing.walk):
#                 thing.walk()
#         print("I think this is a Duck!")
#
#     else:
#         print("I don't think this is a duck!")
#
#
"""
How being more Pythonic can avoid race conditions
"""
# import os
#
# my_file = "file.txt"
#
# if os.access(my_file, os.R_OK):
#     # Race condition could happen here if something happens to the file before
#     # Python is able to open it.
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print("File could not be accessed")
#
# # Non-Race condition
# try:
#     f = open(my_file)
# except IOError as e:
#     print("File could not be accessed")
# else:
#     with f:
#         print(f.read())

"""
Async Tasks
"""
# import time
# import asyncio

# def print_something(something):
#     time.sleep(0.1)
#     print(something)
#
#
# async def print_something_2(something):
#     time.sleep(0.1)
#     print(something)
#
#
# async def main(loop):
#     colors = [
#         "Black",
#         "Yellow",
#         "Green",
#         "Red",
#         "Blue",
#         "Beige",
#         "Orange",
#         "Burgundy",
#         "Pink",
#         "Brown",
#     ]
#     for color in colors:
#         loop.create_task(print_something_2(color))
#
#     # await asyncio.wait()
#
#
# START_TIME = time.clock()
# LOOP = asyncio.get_event_loop()
# try:
#     LOOP.run_until_complete(main(LOOP))
# except Exception as e:
#     pass
# finally:
#     LOOP.close()
# print(f"I took {time.clock() - START_TIME} seconds to complete")
"""
Multiprocessing
"""
# import time
# from multiprocessing import Process, Queue, Pool, cpu_count
# import time

# def print_something(something):
#     time.sleep(1)
#     print(something)
#
#
# def multiprocess_list(items):
#     processes = []
#
#     for item in items:
#         proc = Process(target=print_something, args=(item,))
#         processes.append(proc)
#         proc.start()
#
#     for proc in processes:
#         proc.join()
#
#
# def multiprocess_tasks(tasks, number_of_processes):
#     tasks_to_accomplish = Queue()
#     processes = []
#
#     for task in tasks:
#         tasks_to_accomplish.put(task)
#
#     for i in range(number_of_processes):
#         while not tasks_to_accomplish.empty():
#             p = Process(target=print_something, args=(tasks_to_accomplish.get(),))
#             processes.append(p)
#             p.start()
#
#     for p in processes:
#         p.join()
#
#
# def pool_tasks(tasks, number_of_processes):
#     p = Pool(number_of_processes)
#     p.map(print_something, tasks)
#
#
# COLORS = [
#     "Black",
#     "Yellow",
#     "Green",
#     "Red",
#     "Blue",
#     "Beige",
#     "Orange",
#     "Burgundy",
#     "Pink",
#     "Brown",
# ]
#
# START_TIME = time.time()
# for COLOR in COLORS:
#     print_something(COLOR)
# # Method 1
# multiprocess_list(COLORS) # 1.5 seconds
#
# # Method 2
# multiprocess_tasks(COLORS, cpu_count())  # 1.67 seconds
#
# # Method 3
# pool_tasks(COLORS, cpu_count()) # 3.2 seconds
#
# # No multiprocessing 10 seconds
# for COLOR in COLORS:
#     print_something(COLOR)
#
# print(f"I took {time.time() - START_TIME} seconds to complete")

"""
Python Logging
"""
# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)  # stream_handler will use this level
#
# formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
#
# file_handler = logging.FileHandler("sample.log")
# file_handler.setLevel(logging.ERROR)  # Only write ERRORS to the sample.log
# file_handler.setFormatter(formatter)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
#
# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         logger.exception("Tried to divide by zero")
#
#
# num_1 = 20
# num_2 = 0
#
# divide_result = divide(20, 0)
# logger.debug(f"Divide: {num_1} + {num_2} = {divide_result}")

"""
Github stuff
"""
## discard local commits
# git reset HEAD~
## Discard local changes NOT committed
# git reset --hard
## Compare uncommited files to master
# git diff
## Compare committed changes to master
##git diff --staged
"""
Intertools
"""

## Counter
import itertools

# counter = itertools.count(start=1, step=1)
#
# data = ["Mark", "Ashley", "Christine", "John", "Holiday"]
# combined = list(
#     zip(counter, data)
# )  # zip pairs iterables together, limited by the shortest one.
# print(combined)

## Cycle
# cycle_counter = itertools.cycle(("On", "Off"))  # Good for simulating a switch
# for _ in range(6):
#     print(next(cycle_counter))

## Repeat
# squares = map(pow, range(10), itertools.repeat(2))  # pow(2, 2) == 2^2
# print(list(squares))

## Starmap
# squares = itertools.starmap(
#     pow, [(0, 2), (1, 2), (2, 2)]
# )  # like map(), but takes sets of tuples
# print(list(squares))

## Combinations and Permutations
## With combinations, order does not matter, in permutations, they do.
import time

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
names = ["John", "Ashley"]
# combinations = itertools.combinations(letters, 2)
# permutations = itertools.permutations(letters, 2)

t1 = time.perf_counter_ns()
combined = letters + numbers + names
t2 = time.perf_counter_ns()
CONCAT_TIME = t2 - t1

t3 = time.perf_counter_ns()
combined = itertools.chain(letters, numbers, names)
t4 = time.perf_counter_ns()
CHAIN_TIME = t4 - t3

print(CHAIN_TIME, CONCAT_TIME)
