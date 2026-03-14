import time
import random


class Random_box:
    def randomator(start=50, end=80):
        if start >= end:
            return None

        while True:
            yield random.randint(start, end)

    def time_acc(iterator, timeout):
        start_time = time.time()

        for val in iterator:
            curr_time = time.time()
            if curr_time - start_time > timeout:
                print(f"Time Out: {timeout}")
                break

            print(val)
            time.sleep(0.3)


gen = Random_box.randomator()
Random_box.time_acc(gen, 3)
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


class Random_box2:
    def randomator(start=50, end=80, timeout=3):
        if start >= end:
            return None

        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                print(f"Time Out: {timeout}")
                break

        yield random.randint(start, end)

    def print_val(iterator):
        for val in iterator:
            print(val)
            time.sleep(0.3)


gen = Random_box2.randomator()
Random_box2.print_val(gen)
