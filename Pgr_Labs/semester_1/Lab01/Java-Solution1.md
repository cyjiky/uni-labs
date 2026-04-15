# 👾 Lab01: Scalar value vs Reference & Type Counting
## ✔️ Task 1: Scalar value vs Reference
Подготовьте две реализации функции `inc`:

2. C сигнатурой `inc(n: number): number`,
пример вызова: `const a = 5; const b = inc(a); console.dir({ a, b });`
3. C сигнатурой `inc(num: Num)`, где `Num` является объектом с полем `n`,
чтобы функция изменила поле исходного объекта переданного по ссылке,
пример вызова `const obj = { n: 5 }; inc(obj); console.dir(obj);`

```java
public class Scalar {

    // класс Num в котором содержится поле n
    static class Num {
        int n;

        public Num(int n) {
            this.n = n;
        }
    }

    // Метод inc изменяет поле переданного n объекта
    public static void inc(Num num) {
        num.n++; 
    }

    public static void main(String[] args) {

        // новый объекта Num с полем n = 5
        Num Obj = new Num(5);

        inc(Obj); 

        System.out.println("obj.n: " + Obj.n);
    }
}
```

## ✔️ Task 2: Type Counting
- Создайте исходный массив, содержащий значения различных типов, в качестве
элементов, например: `[true, 'hello', 5, 12, -200, false, false, 'word']`
но желательно более длинный и разнообразный.
- Создайте объект-коллекцию (хеш) с именами типов в виде ключей и `0` в качестве
значения, например: `{ number: 0, string: 0, boolean: 0 }`
- Пройдитесь по массиву циклом `for..of` и для каждого элемента массива,
увеличивайте соответствующее значение в объекте-коллекции.
- Измените пример: удалите все ключи из начальной коллекции и добавляйте их
динамически в цикле.

```java
import java.util.HashMap; 
import java.util.Map;

public class Main { 
    public static void main(String[] args) {
        Object[] arr = { true, "hello", 5, 12, -200, false, false, "word" };
        Map<String, Integer> type = new HashMap<>();

        // цикл "for-each"
        // перебирает значения массива arr и каждый елемент присваивает elem
        for (Object elem : arr) {
            String name;

            // цикл "if-else"
            if (elem == null) { //
                name = "null";
            } else {
                name = elem.getClass().getSimpleName();
            }

            // подсчёт ключ (String/Boolean) с библиотеки и добавляет +1 (увеличивает счётчик)
            type.put(name, type.getOrDefault(name, 0) + 1);
            // type.put -> обновляет и добавляет значение в Map
        }

        // используется лямба
        // метод "for-each"
        type.forEach((key, value) -> System.out.println(key + ": " + value));

    }
}
```









