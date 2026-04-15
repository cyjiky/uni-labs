from datetime import datetime


def func_decorator(cache_size = -1):
    def decorator(func):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in cache:
                print(f"Cache: {cache[key]}")
                cache[key]["data"] = datetime.now()
                return cache[key]["cache"]
            else:
                if len(cache) >= cache_size and not cache_size < 1:
                    cache_arr = list(cache.items())
                    cache_arr.sort(key=lambda cached: cached[1]["data"])
                    del cache[cache_arr[0][0]]

                new_cache = func(*args, **kwargs)
                cache[key] = {"cache": new_cache, "data": datetime.now()}
                print(f"New cache: {new_cache}")
                return new_cache

        return wrapper

    return decorator


@func_decorator(cache_size=20)
def sum(x: int, y: int) -> int:
    return x + y


sum(2, 4)
sum(2, 4)
