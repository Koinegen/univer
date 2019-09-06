import math
import time

def _random_base(m, y):
    return (1664525 * y + 1) % m


def random(after_dot: int = 5, count: int = 10):
    main_list = []
    y = time.time() % 1
    print(y)
    m = 2 ** 32
    for i in range(count):
        result = _random_base(m, y) % 1
        y = result
        result = float('{:.{}f}'.format(result, after_dot))
        main_list.append(result)
    return main_list






if __name__ == '__main__':
    print(random())