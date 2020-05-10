import time
import os
import logging

# """
# Idempotence
# f(f(x)) = f(x)
#
# Whenever you do something over and over again, you get the same result.
#
# GET
# PUT
# POST
# DELETE
#
# Are always Idempotent
#
# POST is NOT Idempotent (The response can change on multiple tries)
# """
#
# print(abs(abs(-10)))  # Will always be 10
#
# """
# Closures
#
# "A closure is an inner function that remembers and has access to variables in
# the local scope in which it was created.
# """
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
# """
# Memoization: storing the result of a function so it does not need to be re-run
# if the same inputs are seen again.
# """
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
# """
# Ternary Conditional
# """
# # condition = False
# # x = 1 if condition else 0
#
# """
# formatting large numbers.
# 2_000_000 # Adding underscores does not affect numbers in Python!
# """
# num1 = 10_000_000_000
# num2 = 100_000_000
# total = num1 + num2
#
# print(f"{total:,}")
#
# """
# iterate over two lists at once!
# """
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
# """
# Tuple unpacking
# """
# # set 'a' and 'b' to 1, 2 and c to everything up to the last one [3, 4] d to 5
# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a, b, c, d)
# # Ignore the rest of the arguments completely
# a, b, *_ = (1, 2, 3, 4, 5)
# print(a, b, c, d)
#
# """
# Being 'Pythonic'... EAFP (Easier to ask forgiveness than permission)
# 'Let's try to do something and if it doesn't work, we will handle it.
# vs
# Look before you leap (LBYL)
# 'ask permission every step you take.'
#
# Python can be a lot faster in situations where you don't expect a lot of errors
# because you don't have to keep accessing the object to ask it questions before
# proceeding.
# """
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
# """
# How being more Pythonic can avoid race conditions
# """
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
Python Logging
"""

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug(f"Add: {num_1} + {num_2} = {add_result}")
