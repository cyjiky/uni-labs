# Реализуйте интроспекцию объекта:
# Проитерируйте все ключи объекта iface
# Возьмите ключи функционального типа
# Для каждой функции возьмите 
#   количество аргументов
# Сохраните результаты в двумерный массив

"""
{
  m1: x => [x],
  m2: function (x, y) {
    return [x, y];
  },
  m3(x, y, z) {
    return [x, y, z];
  }
}
"""

"""
[
  ['m1', 1],
  ['m2', 2],
  ['m3', 3]
]
"""

iface = {
  'm1': lambda x: x + 2,
  'm2': lambda x, y: (x + y) / 2,
  'm3': lambda x, y, z: x * y * z 
}

def count_arg(key: str) -> int: 
  return iface[key].__code__.co_argcount

print(count_arg('m2'))