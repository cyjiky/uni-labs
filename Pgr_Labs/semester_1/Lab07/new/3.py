# Функция difference(array1, array2) должна
#   находить разницу между массивами, т.е.
#   возвращать новый массив, содержащий значения,
#   которые содержались в array1, но не содержались
#   в array2. Примеры вызова:

"""
const array1 = [7, -2, 10, 5, 0];
const array2 = [0, 10];
const result = difference(array1, array2);
console.log(result);
// Результат: [7, -2, 5]
"""

"""
const array1 = ['Beijing', 'Kiev'];
const array2 = ['Kiev', 'London', 'Baghdad'];
const result = difference(array1, array2);
console.log(result);
// Результат: ['Beijing']
"""
from typing import List

arr1 = [7, -2, 10, 5, 0]
arr2 = [0, 10]

arr1_1 = ["Beijing", "Kiev"]
arr2_2 = ["Kiev", "London", "Baghdad"]


def difference(f_arr: List, s_arr: List) -> List:
    return [el for el in f_arr if el not in set(s_arr)]


print(difference(arr1, arr2))
print(difference(arr1_1, arr2_2))
