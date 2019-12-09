import csv


def output_csv(**kwargs):
    with open('lab6_out.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        # all_data = []
        # keys = [key for key in kwargs.keys()]
        # all_data.append(keys)
        for key in kwargs.keys():
            writer.writerow(kwargs.get(key))
