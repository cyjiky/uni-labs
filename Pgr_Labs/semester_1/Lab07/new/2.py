# Функция unique(array) должна возвращать 
#   новый массив, не содержащий дубликатов. Примеры вызова:
"""
const result = unique([2, 1, 1, 3, 2]);
console.log(result);
// Результат: [2, 1, 3]
"""
"""
const result = unique(['top', 'bottom', 'top', 'left']);
console.log(result);
// Результат: ['top', 'bottom', 'left']
"""

from typing import List 

arr1 = [2, 1, 1, 3, 2]
arr2 = ['top', 'bottom', 'top', 'left']

def unique1(arr: List) -> List: 
    arr_ = []
    for i in arr:
        if i not in arr_:
            arr_.append(i)
    return arr_

def unique2(arr: List) -> List: 
    return list(dict.fromkeys(arr).keys())

print(unique1(arr1))
print(unique2(arr2))

# print(set(arr1))