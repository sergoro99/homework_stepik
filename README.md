# Декораторы в Python

Этот репозиторий содержит реализацию нескольких полезных декораторов в Python, которые демонстрируют различные возможности декораторов и показывают, как их можно использовать для решения конкретных задач.

## Содержание

1.  [Описание](#описание)
2.  [Установка](#установка)
3.  [Использование](#использование)
    *   [`@benchmark`](#benchmark)
    *   [`@logging`](#logging)
    *   [`@counter`](#counter)
    *   [`@memo`](#memo)
4. [Комбинация декораторов](#комбинация-декораторов)
5.  [Пример с числами Фибоначчи](#пример-с-числами-фибоначчи)
6.  [Лицензия](#лицензия)

## Описание

В этом репозитории представлены четыре пользовательских декоратора:

*   `@benchmark`: измеряет и выводит время выполнения декорируемой функции.
*   `@logging`: выводит параметры, с которыми была вызвана декорируемая функция.
*   `@counter`: считает и выводит количество вызовов декорируемой функции.
*   `@memo`: мемоизирует (кэширует) результаты выполнения декорируемой функции для хешируемых аргументов, позволяя избежать повторных вычислений.

Эти декораторы могут быть полезны при отладке кода, оптимизации производительности и для более глубокого понимания работы функций.

## Установка

1.  Склонируйте репозиторий на свой компьютер:

    ```bash
    git clone <URL_вашего_репозитория>
    ```

2.  Перейдите в директорию репозитория:

    ```bash
    cd <имя_директории_репозитория>
    ```

## Использование

### `@benchmark`

Декоратор `@benchmark` измеряет и выводит время выполнения декорируемой функции. Это может быть полезно для анализа производительности вашего кода.

**Пример:**

```python
import time
from decorators import benchmark

@benchmark
def slow_function(n):
    time.sleep(n)

slow_function(0.5)
Вывод:

Function 'slow_function' took 0.501 seconds to execute
@logging
Декоратор @logging выводит параметры, с которыми была вызвана декорируемая функция, для отладки и логирования.

Пример:

from decorators import logging

@logging
def my_function(a, b, c="default"):
  print(f"Hello, my function {a} {b} {c}")

my_function(1, 2, c="custom")
Вывод:

Function 'my_function' called with arguments: (1, 2), {'c': 'custom'}
@counter
Декоратор @counter подсчитывает и выводит количество вызовов декорируемой функции. Это может быть полезно для мониторинга использования функций.

Пример:

from decorators import counter

@counter
def my_function(x):
    return x * 2

my_function(5)
my_function(10)
my_function(15)
Вывод:

Function 'my_function' called 1 times
Function 'my_function' called 2 times
Function 'my_function' called 3 times
@memo
Декоратор @memo мемоизирует (кэширует) результаты выполнения декорируемой функции для хешируемых аргументов, позволяя избежать повторных вычислений. Он использует словарь для хранения результатов.

Пример:

import time
from decorators import memo

@memo
def fibonacci(n):
  if n <= 1:
    return n
  time.sleep(0.2)
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6)) # Первый вызов
print(fibonacci(6)) # Второй вызов возвращается из кэша
print(fibonacci(7)) # Первый вызов с другими аргументами
Вывод:

Calculating result for arguments (6,)
Calculating result for arguments (5,)
Calculating result for arguments (4,)
Calculating result for arguments (3,)
Calculating result for arguments (2,)
Calculating result for arguments (1,)
Calculating result for arguments (0,)
Result for arguments (0,) found in cache
Result for arguments (1,) found in cache
Result for arguments (2,) found in cache
Result for arguments (3,) found in cache
Result for arguments (4,) found in cache
Result for arguments (5,) found in cache
8
Result for arguments (6,) found in cache
8
Calculating result for arguments (7,)
Result for arguments (6,) found in cache
Result for arguments (5,) found in cache
13
Комбинация декораторов
Декораторы можно комбинировать, чтобы применять несколько эффектов к одной функции. В следующем примере показано, как работают @counter, @logging, и @benchmark одновременно.

Пример:

import requests
import re
from time import sleep
from decorators import benchmark, logging, counter

@counter
@logging
@benchmark
def word_count(word, url='https://www.gutenberg.org/files/2638/2638-0.txt'):
    
    # отправляем запрос в библиотеку Gutenberg и забираем текст
    raw = requests.get(url).text

    # заменяем в тексте все небуквенные символы на пробелы
    processed_book = re.sub('[\W]+' , ' ', raw).lower()
    
    # считаем
    sleep(0.2)
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"

print(word_count('whole'))
print(word_count('whole'))
Вывод:

Function 'word_count' called with arguments: ('whole',), {}
Function 'word_count' took 0.471 seconds to execute
Function 'word_count' called 1 times
Cлово whole встречается 243 раз
Function 'word_count' called with arguments: ('whole',), {}
Function 'word_count' took 0.306 seconds to execute
Function 'word_count' called 2 times
Cлово whole встречается 243 раз
Пример с числами Фибоначчи
Для демонстрации эффективности @memo был протестирован расчет чисел Фибоначчи. Мемоизация значительно сокращает время выполнения, избегая многократного пересчета уже вычисленных значений. Для более детального тестирования вы можете убрать декоратор @memo и оценить время вычисления чисел Фибоначчи, например, 25.
