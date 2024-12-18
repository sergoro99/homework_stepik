import requests
import time
import re

from random import randint

BOOK_PATH = 'https://www.gutenberg.org/files/2638/2638-0.txt'


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        res_time = time.time() - start
        print(f'Время выполнения функции {func.__name__}: {res_time:.6f}')
        return result

    return wrapper


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
        print(f'Функция вызвана с параметрами:\n{args}, {kwargs}')
        result = func(*args, **kwargs)
        return result

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    c = 0

    def wrapper(*args, **kwargs):
        nonlocal c
        c += 1
        print(f'Функция была вызвана: {c} раз')
        result = func(*args, **kwargs)
        return result

    ...
    return wrapper


def memo(func):
    """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
    cache = {}

    def fmemo(*args):
        if args in cache:
            result = cache[args]
            print(f'Результат по данным аргументам {args} есть в памяти')
            return result
        result = func(*args)
        cache[args] = result
        return result

    fmemo.cache = cache
    return fmemo


@counter
@logging
@benchmark
def word_count(word, url=BOOK_PATH):
    """
    Функция для посчета указанного слова на html-странице
    """

    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+', ' ', raw).lower()

    # считаем
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"


print(word_count('whole'))


@memo
@benchmark
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


print(fib(10))
