import unittest
import time
from functools import reduce
from unittest.mock import patch
from io import StringIO
from MyPythonCourse.practice.Lesson_3.task1 import *
from MyPythonCourse.practice.Lesson_3.task2 import *
from MyPythonCourse.practice.Lesson_3.task3 import *
from MyPythonCourse.practice.Lesson_3.task4 import *
from MyPythonCourse.practice.Lesson_3.task5 import *
from MyPythonCourse.practice.Lesson_3.task6 import *
from MyPythonCourse.practice.Lesson_3.task7 import *
from MyPythonCourse.practice.Lesson_3.task8 import *
from MyPythonCourse.practice.Lesson_3.task9 import *



# Импорт ваших функций (замените на реальные имена файлов/модулей)
# from your_module import (
#     add_numbers, is_even, factorial, count_vowels, sum_all,
#     sum_and_product, fibonacci, square_list, apply_function,
#     create_counter, timer, repeat, flatten_sum
# )

# Реализации функций (временные, для тестирования)
# def add_numbers(a, b): return a + b
#
#
# def is_even(n): return n % 2 == 0
#
#
# def factorial(n): return 1 if n == 0 else n * factorial(n - 1) if n > 0 else None
#
#
# def count_vowels(s): return sum(1 for c in s.lower() if c in 'aeiou')
#
#
# def sum_all(*args): return sum(args)
#
#
# def sum_and_product(lst): return (sum(lst), reduce(lambda x, y: x * y, lst, 1))
#
#
# def fibonacci(n): return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
#
#
# def square_list(lst): return list(map(lambda x: x ** 2, lst))
#
#
# def apply_function(func, lst): return list(map(func, lst))
#

def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Время выполнения: {time.time() - start:.2f} сек.")
        return result

    return wrapper


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


def flatten_sum(nested_list):
    if isinstance(nested_list, list):
        return sum(flatten_sum(item) for item in nested_list)
    return nested_list


class TestFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        print("test_add_numbers passed")
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-3))
        print("test_is_even passed")
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertIsNone(factorial(-1))
        print("test_factorial passed")
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("BCDFG"), 0)
        self.assertEqual(count_vowels("AaEeIiOoUu"), 10)
        print("test_count_vowels passed")
    def test_sum_all(self):
        self.assertEqual(sum_all(1, 2, 3, 4), 10)
        self.assertEqual(sum_all(), 0)
        self.assertEqual(sum_all(-5, 5), 0)
        print("test_sum_all passed")
    # def test_sum_and_product(self):
    #     self.assertEqual(sum_and_product([2, 3, 4]), (9, 24))
    #     self.assertEqual(sum_and_product([5]), (5, 5))
    #     self.assertRaises(TypeError, sum_and_product, [])

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(7), 13)
        print("test_fibonacci passed")
    def test_square_list(self):
        self.assertEqual(square_list([1, 2, 3, 4]), [1, 4, 9, 16])
        self.assertEqual(square_list([-2, 3]), [4, 9])
        self.assertEqual(square_list([]), [])
        print("test_square_list passed")
    def test_apply_function(self):
        self.assertEqual(apply_function(lambda x: x * 2, [1, 2, 3]), [2, 4, 6])
        self.assertEqual(apply_function(lambda x: x ** 2, [3, 4]), [9, 16])
        print("test_apply_function passed")
    def test_create_counter(self):
        counter1 = create_counter()
        self.assertEqual(counter1(), 1)
        self.assertEqual(counter1(), 2)

        counter2 = create_counter()
        self.assertEqual(counter2(), 1)
        print("test_create_counter passed")
    # def test_timer_decorator(self):
    #     @timer
    #     def test_func():
    #         time.sleep(0.5)
    #
    #     with patch('sys.stdout', new=StringIO()) as fake_out:
    #         test_func()
    #         output = fake_out.getvalue()
    #         self.assertTrue("Время выполнения: 0.50 сек." in output)

    def test_repeat_decorator(self):
        @repeat(3)
        def test_func():
            print("Test")

        with patch('sys.stdout', new=StringIO()) as fake_out:
            test_func()
            self.assertEqual(fake_out.getvalue().count("Test\n"), 3)

    def test_flatten_sum(self):
        self.assertEqual(flatten_sum([1, [2, [3, 4], 5], 6]), 21)
        self.assertEqual(flatten_sum([[[]]]), 0)
        self.assertEqual(flatten_sum([10, [-5, 3]]), 8)


if __name__ == '__main__':
    unittest.main()
