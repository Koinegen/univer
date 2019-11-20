import time


def _random_base(y):
    return (1664543 * y + 1) % 1664501


def random(after_dot: int = 5, count: int = 10):
    main_list = []
    y = time.time() % 1
    print(y)
    for i in range(count):
        result = _random_base(y) % 1
        y = result
        result = float('{:.{}f}'.format(result, after_dot))
        main_list.append(result)
    return main_list






if __name__ == '__main__':
    print(random())