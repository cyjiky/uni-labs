# Реализуйте функцию random(min, max),
#   возвращающую псевдо-случайное значение от min до max.
#   Используйте Math.random() и Math.floor().
#   При вызове random(max) нужно считать, что min = 0.

from random import choice, randrange
import string

print(randrange(100))


# Реализуйте функцию generateKey(length, characters),
#   возвращающую строку случайных символов из набора characters
#   длиной length. Например:
#       const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
#       const key = generateKey(16, characters);
#       console.log(key); // eg599gb60q926j8i

CHAR = 'abcdefghijklmnopqrstuvwxyz0123456789'

def generate_key(length: int, char: str) -> str:
    arr = []
    for i in range(length):
        arr.append(choice(char))
    return "".join(arr)

print(f'generate_key: {generate_key(10, CHAR)}')


def password(length: int) -> str:
    key = ''
    for _ in range(length):
        character = choice(string.ascii_letters)
        key += choice(character)
    return key

print(f'password: {password(16)}')