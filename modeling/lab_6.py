from univer.modeling.lib.BRV import random
from math import e
from univer.modeling.lib.lib_func_for_6_lab import table_output


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
    prev = 0
    for i in random_list:
        a = CalendarLine(i, prev, lambd=lambd, t_obs=t_obs)
        return_list.append(a)
        prev = a.get_t0()
    return return_list


t_wait = []
t_in = []
t_sys = []
L = 0


def create_threads(count=2):
    return [{"time": 0} for _ in range(count)]


req_list = generate_list(count, lambd, t_obs)
threads_inst = create_threads()


def get_min_time_thread():
    time = 99999999
    link = None
    for i in threads_inst:
        print(i)
        if i.get("time") <= time:
            time = i.get("time")
            link = i
    return link


for num, req in enumerate(req_list):
    if num == 0:
        t_wait.append(0)
        t_in.append(req.get_tobs())
        get_min_time_thread()["time"] += req.get_t0() + req.get_tobs()
        t_sys.append(req.get_t0() + req.get_tobs())
    else:
        min_que = get_min_time_thread()
        if min_que.get("time") < req.get_t0():
            t_wait.append(0)
            min_que['time'] += req.get_tobs() + req.get_t0()
            t_sys.append(min_que['time'])
            t_in.append(t_sys[num] - req.get_t0())
            print('check1')
            continue
        if min_que.get("time") > req.get_t0():
            t_wait.append(min_que.get('time') - req.get_t0())
            min_que["time"] += req.get_tobs() + t_wait[num]
            t_sys.append(min_que["time"])
            t_in.append(t_sys[num] - req.get_t0())
            print('check2')
            continue

table_output(count=count, t0=[i.get_t0() for i in req_list], t_obs=[i.get_tobs() for i in req_list],
             t_wait=t_wait, t_in=t_in, t_sys=t_sys)
