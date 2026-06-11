# Реализуйте функцию iterate(object, callback)
#   которая будет итерировать все ключи
#   переданного объекта, вызывая для каждого
#   callback со следующим контрактом
#   callback(key, value, object).
#   Например:

"""
const obj = { a: 1, b: 2, c: 3 };
iterate(obj, (key, value) => {
  console.log({ key, value });
});
"""

# Вывод:

"""
{ key: 'a', value: 1 }
{ key: 'b', value: 2 }
{ key: 'c', value: 3 }
"""
from typing import Callable, Dict

arr = {"a": 1, "b": 2, "c": 3}


def iterate(obj: Dict, callback: Callable[[str, int, Dict], None]):
    for k, v in obj.items():
        callback(k, v, obj)


def print_dicts(k, v, obj):
    print(dict(key=k, value=v))


iterate(arr, print_dicts)