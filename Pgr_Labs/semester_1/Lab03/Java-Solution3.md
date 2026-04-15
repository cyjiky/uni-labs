# 👾 Lab03: Functions, lambda-functions, function contexts, closures

✔️ Реализуйте функцию `random(min, max)`, возвращающую псевдо-случайное
значение от `min` до `max`. Используйте `Math.random()` и `Math.floor()`.
При вызове `random(max)` нужно считать, что `min = 0`

```java
import java.util.Random;

public class Aufgabe12 {
    public static void main(String[] args) {

        // 1.
        int min = 0;
        int max = 100;

        Random random = new Random();
        int randomNum = random.nextInt((max - min) + 1) + min;

        System.out.println("Random number 1: " + randomNum);

        // 2.
        double randomValue = Math.random();
        System.out.println("Random number 2: " + randomValue);

        // 3.
        int randomInt = (int) Math.floor(Math.random() * (max - min + 1) + min);
        System.out.println("Random number 3: " + randomInt);
    }
}

```

✔️ Реализуйте функцию `generateKey(length, characters)`, возвращающую строку
случайных символов из набора `characters` длиной `length`

```java
public class Main {
    public static void main(String[] args) {
        double a = 5.09843895;
        double result = Math.floor(a);
        System.out.println(result);
    }
}

```

✔️Преобразуйте IP адрес (IPv4) в число, содержащее 4 байта адреса,
сдвинутые битовым сдвигом, по такой схеме:
- 1 байт сдвинут 3 раза на 8 бит влево
- 2 байт сдвинут 2 раза на 8 бит влево
- 3 байт сдвинут 1 раз на 8 бит влево
- 4 байт не сдвинут
Например: '10.0.0.1':
- Преобразовываем строку `'10.0.0.1'` в массив `['10', '0', '0', '1']`
- Преобразовываем массив `['10', '0', '0', '1']` в массив `[10, 0, 0, 1]`
- Сдвигаем все элементы по приведенной схеме при помощи цикла:
`[10 << 8 << 8 << 8, 0 << 8 << 8, 0 << 8, 1]` и получаем `[167772160, 0, 0, 1]`
- Суммируем все элементы и получаем `167772161`
- Оптимизируем код через использование `Array.prototype.reduce`
Используйте значение аргумента функции по умолчанию '127.0.0.1'.

```java
public class IP {
    public static int ipToNumber(String ip) {
        String[] parts = ip.split("\\.");
        // split("\\.") делит строку на миссив строк
        int result = 0;

        for (int i = 0; i < 4; i++) {
            result += Integer.parseInt(parts[i]) << ((3 - i) * 8);
            // метод Integer.parseInt() переобразовавывает строку в целое число
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(ipToNumber("127.0.0.1")); // 2130706433
        System.out.println(ipToNumber("10.0.0.1")); // 167772161
        System.out.println(ipToNumber("192.168.1.10")); // -1062731510
        System.out.println(ipToNumber("165.225.133.150")); // -1511946858
        System.out.println(ipToNumber("0.0.0.0")); // 0

        System.out.printf("0x%08X\n", ipToNumber("8.8.8.8")); // 0x08080808
    }
}

```

✔️ Реализуйте интроспекцию объекта:
- Проитерируйте все ключи объекта `iface`
- Возьмите ключи функционального типа
- Для каждой функции возьмите количество аргументов
- Сохраните результаты в двумерный массив


```java
// первая часть
import java.lang.reflect.Method;
 
public class Main {
    public static void main(String[] args) {
        MyClass iface = new MyClass();
 
        Method[] methods = iface.getClass().getDeclaredMethods();
 
        int[][] result = new int[methods.length][];
 
        for (int i = 0; i < methods.length; i++) {
            int ParamCount = methods[i].getParameterCount();
 
            result[i] = new int[] { ParamCount };
        }
 
        for (int i = 0; i < result.length; i++) {
            // System.out.println("In Methode " + methods[i].getName() + " gibt es " +
            // result[i][0] + " Parameter.");
            System.out.println("['" + methods[i].getName() + "', " + result[i][0] + "']");
        }
    }
}

```
```java
// вторая часть
public class MyClass {
    public Object m1(Object x) {
        return new Object[] { x };
    }
 
    public Object m2(Object x, Object y) {
        return new Object[] { x, y };
    }
 
    public Object m3(Object x, Object y, Object z) {
        return new Object[] { x, y, z };
    }
}

```
