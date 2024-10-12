# Задание 2.
# Добавьте к первому заданию возможность передавать границы диапазона для поиска всех простых чисел.
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
def list_prime_numbers(start, end):
    prime_numbers = []
    for i in range(start, end + 1):
        if all(i % j != 0 for j in range(2, i)):
            prime_numbers.append(i)
    return prime_numbers


print(list_prime_numbers(2, 4500))