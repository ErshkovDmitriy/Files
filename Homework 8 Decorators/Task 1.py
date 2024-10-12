# Задание 1.
# Создайте функцию, возвращающую список со всеми простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.
import time


def time_worker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f'Функция {func.__name__} выполнялась {end} сек.')
        return result

    return wrapper


@time_worker
def list_prime_numbers():
    prime_numbers = []
    for i in range(2, 10000):
        if all(i % j != 0 for j in range(2, i)):
            prime_numbers.append(i)
    return prime_numbers


print(list_prime_numbers())
