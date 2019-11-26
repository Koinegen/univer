from univer.modeling.lib.BRV import random
from math import e


class CalendarLine:

    def __init__(self, arr_time, prev_time=None, lambd = 1, t_obs=2):
        self.z = arr_time
        self.lambd = lambd
        if prev_time == None:
            prev_time = 0
        self.t0 = self._set_t0() + prev_time
        self.mu = 1 / t_obs
        self.t_obs = self._set_tobs()

    def _set_tobs(self):
        a = -(self.mu * self.z)
        return 1 - e ** a

    def _set_t0(self):
        a = -(self.lambd * self.z)
        return 1 - e**a

    def get_tobs(self):
        return self.t_obs

    def get_t0(self):
        return self.t0


threads = 2
t_obs = 2
queue = 4
lambd = 1
count = 500
"""
:param threads: Кол-во потоков (Не меньше 1)
:param queue:
Очередь: None-бесконечная очередь;
0 - Очереди нет, все приходящие заявки, которые не могут быть обслуженными отбрасываются
Любое целое число - очередь длинной с заданное число.
:param lambd: Плотность потока.
:param count: 
"""


def generate_list(count, lambd=1, t_obs=2):
    return_list = []
    random_list = random(count=count)
    for i in random_list:
        prev = 0
        return_list.append(CalendarLine(i, prev, lambd=lambd, t_obs=t_obs))
    return return_list


t_wait = []
t_in = []
t_sys = []
L = 0


def create_threads(count=2):
    return [{i: 0} for i in range(count)]


req_list = generate_list(count, lambd, t_obs)
threads_inst = create_threads()


#for num, req in enumerate(req_list):



