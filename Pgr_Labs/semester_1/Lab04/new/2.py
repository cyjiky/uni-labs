"""
Найдите максимальный элемент в двумерном массиве
const m = max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
console.log(m); // 9
"""

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max_ = float(str('-inf'))
for i in m:
    for j in i:
        if j > max_:
            max_ = j 
        
print(max_)