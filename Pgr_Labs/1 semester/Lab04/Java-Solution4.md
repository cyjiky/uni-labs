# 👾 Lab04: Different implementation of iterations as a code abstraction
## ✔️ Итерирование циклами

Реализуйте функцию `sum(...args)`, которая суммирует все свои аргументы, пятью
разными способами. Примеры вызовов с результатами: 6, 0, 0, 1, 7

1. Цикл `for`
2. Цикл `for..of`
3. Цикл `while`
4. Цикл `do..while`
5. Метод `Array.prototype.reduce()`

```java
import java.util.HashMap;
import java.util.Map;

public class Lab {
    public static void main(String[] args) {
        Integer[] a = { 1, 2, 3 }; // 6
        Integer[] b = { 0 }; // 0
        Integer[] c = {}; // 
        Integer[] d = { 1, -1, 1 }; // 1
        Integer[] e = { 10, -1, -1, -1 }; // 7

        // 1. for
        int i = 0;
        int sum = 0;

        for (i = 0; i < a.length; i++) {
            sum += a[i];
        }
        System.out.println(sum);

        // 2. for-each (for..of in js)
        sum = 0;

        for (int elem : b) {
            sum += elem;
        }
        System.out.println(sum);

        // 3. while
        i = 0;
        sum = 0;
        while (i < c.length) {
            System.out.println(i);
            i++;
        }

        // 4. do..while
        i = 0;
        do {
            sum += d[i];
            i++;
        } while (i < d.length);
        System.out.println(sum);

        // 5. на подобии метода Array.prototype.reduce()
```
## ✔️ Найдите максимальный элемент в двумерном массиве
```
{ { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } } // 9
```

```java
        // 6. нахождение максимального елемента в двумерном массиве
        Integer[][] max = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };

        int maxValue = Integer.MIN_VALUE;

        for (int u = 0; u < max.length; u++) {
            for (int j = 0; j < max[u].length; j++) {
                if (max[u][j] > maxValue) {
                    maxValue = max[u][j];
                }
            }
        }
        System.out.println("maxValue: " + maxValue);
    }
```
## ✔️ При помощи цикла `for..in` перебрать объект-справочник с датами рождения и смерти людей и вернуть справочник с продолжительностью их жизни
```java
    // 7. перебор объекта-справочника с помощью цикла for..in

    // класс для хранения данных
    static class Person {
        int born;
        int died;

        Person(int born, int died) {
            this.born = born;
            this.died = died;
        }
    }

    // использование функции Map<>
    public static Map<String, Integer> ages(Map<String, Person> persons) {
        Map<String, Integer> result = new HashMap<>();

        for (String key : persons.keySet()) {
            Person p = persons.get(key);
            int age = p.died - p.born;
            result.put(key, age);
        }
        return result;
    }

    // вывод
    public static void Main(String[] args) {
        Map<String, Person> persons = new HashMap<>();
        persons.put("Lenin", new Person(1870, 1924));
        persons.put("Mao", new Person(1893, 1976));
        persons.put("Gandhi", new Person(1869, 1948));
        persons.put("Hirohito", new Person(1901, 1989));

        Map<String, Integer> result = ages(persons);

        for (String name : result.keySet()) {
            System.out.println(name + ": " + result.get(name));
        }
    }

}
```
