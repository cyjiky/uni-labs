# Вложенные вызовы функций в цикле


# Реализуйте функцию average с сигнатурой average(a: number, b: number):
#   number вычисляющую среднее арифметическое своих аргументов.


def avg(a: int | float, b: int | float) -> float:
    return (a + b) / 2


avg_ = lambda a, b: (a + b) / 2
# print(f"avg_: {avg_(2, 4)}")


# Реализуйте функцию square с сигнатурой square(x: number):
#   number вычисляющую квадрат своего аргумента.


def sqr_(x: int | float) -> float:
    return x**2


sqr_2 = lambda x: x**2
# print(f'sqr_2: {sqr_2(3)}')


# Реализуйте функцию cube с сигнатурой cube(x: number):
#   number вычисляющую куб своего аргумента.


def cub(x: int | float) -> float:
    return pow(x, 3)


cub2 = lambda x: x**3
# print(f'cub2: {cub2(2)}')


# Вызовите функции square и cube в цикле от 0 до 9, вычисляя,
#   соответственно квадрат и куб от переменной цикла.
#   Передайте квадрат и куб на каждой итерации в функцию average.
#   Результаты сложите в массив и возвратите из функции calculate.
def calculate() -> list:
    res = []
    for i in range(10):
        res.append(avg(a=sqr_(i), b=cub(i)))

    return res


print(calculate())
