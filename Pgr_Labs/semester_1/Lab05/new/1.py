# Реализуйте функцию seq(...args) с
#   использованием замыканий и чеининга,
#   которая может быть вызвана по цепочке
#   с произвольным количеством функций, а
#   первый вызов со значением типа Number
#   приведет к исполнению переданных ранее
#   функций и возвращаемый результат должен
#   быть, как в приведенных примерах:

"""
seq(x => x + 7)
   (x => x * 2)(5)

// Результат: 17
"""


def sq1(x):
    x *= 2

    def fn():
        return x + 7

    return fn


# print(sq1(5)())


"""
seq(x => x * 2)
   (x => x + 7)(5)

// Результат: 24
"""


def sq2(x):
    x += 7

    def fn():
        return x * 2

    return fn


# print(sq2(5)())

"""
seq(x => x + 1)
   (x => x * 2)
   (x => x / 3)
   (x => x - 4)(7)

// Результат: 3
"""
from typing import Callable

def seq(func_) -> Callable:
    fc = [func_]  # fc = [<func *2>, <func +7>]

    def func(arg) -> Callable | float:
        if isinstance(arg, (int)):
            val = arg
            for i in fc[::-1]:
                val = i(val)
            return val
        fc.append(arg)
        return func

    return func


res = seq(lambda x: x + 1)(lambda x: x * 2)(lambda x: x / 3)(lambda x: x - 4)(7)
print(res)
