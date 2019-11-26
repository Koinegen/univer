from prettytable import PrettyTable



def table_output(**kwargs):
    x = PrettyTable()
    x.add_column("N", range(1, kwargs.get("count") + 1))
    x.add_column("T_0", kwargs.get("t0"))
    x.add_column("T_ожидания", kwargs.get("t_wait"))
    x.add_column("T_прибывания", kwargs.get("t_in"))
    x.add_column("T_системное", kwargs.get("t_sys"))
    x.add_column("T_обслуживания", kwargs.get("t_obs"))
    print(x)


