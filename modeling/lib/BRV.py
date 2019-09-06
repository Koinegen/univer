import math
import time

def _random_base(a, m, y, c):
    return (1664525 * y + 1) % m


def random(after_dot: int = 5, count: int = 10):
    main_list = []
    nod_dict = {
        5: {"c": 33343, "m": 2 ** 32},
        4: {"c": 7789, "m": 2 ** 32},
        3: {"c": 557, "m": 2 ** 32},
        2: {"c": 11, "m": 2 ** 32},
        1: {"c": 7, "m": 2 ** 32}
    }
    y = time.time() % 1
    #y = float('{:.1f}'.format(y))
    print(y)
    c = nod_dict.get(after_dot).get("c")
    m = nod_dict.get(after_dot).get("m")
    for i in range(count):
        result = _random_base(3, m, y, c) % 1
        y = result
        result = float('{:.5f}'.format(result))
        main_list.append(result)
    return main_list






if __name__ == '__main__':
    print(random())