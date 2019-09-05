import math
import time


def _random_base(a, m, y):
    return (a * y + m) % m


def random(after_dot: int = 5, count: int = 10):
    main_list = []
    nod_dict = {
        5: {"a": 33333, "m": 100000},
        4: {"a": 7777, "m": 10000},
        3: {"a": 999, "m": 1000},
        2: {"a": 11, "m": 100},
        1: {"a": 7, "m": 10}
    }
    y = time.time() % 1
    y = float('{:.1f}'.format(y))
    print(y)
    for i in range(count):
        result = (_random_base(nod_dict.get(after_dot).get("a"), nod_dict.get(after_dot).get("m"), y)) % 1
        main_list.append(result)
        y = float('{:.1f}'.format(result))
    return main_list






if __name__ == '__main__':
    print(random(1))