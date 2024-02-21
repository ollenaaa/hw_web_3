import multiprocessing
import time
import logging
from multiprocessing import Pool

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def sync_factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def async_factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


if __name__ == '__main__':
    start_time = time.time()
    a, b, c, d = sync_factorize(128, 255, 99999, 10651060)
    end_time = time.time()

    print(f"Синхронне виконання зайняло {end_time - start_time} секунд")

    start_time = time.time()
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        logger.debug(pool.map(async_factorize, (128, 255, 99999, 10651060)))
    end_time = time.time()

    print(f"Асинхронне виконання зайняло {end_time - start_time} секунд")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]