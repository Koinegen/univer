from prettytable import PrettyTable



def table_output(vars_dict: dict):
    count = len(vars_dict.keys())
    table_head = ''.join("|\t{}\t|".format(i) for i in vars_dict.keys())
    second_str = ''.join("||" for _ in vars_dict.keys())
    print(table_head)
    print(second_str)



dt = {
    1: "gfk",
    2: "gk",
    3: "gkgf",
    4: "gkw",
    5: "gk31",
    6: "gk3",
    7: "gk435"
}
table_output(dt)