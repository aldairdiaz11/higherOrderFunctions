import csv
from functools import reduce


def count(predicate: bool, itr) -> int:
    count_filter = filter(predicate, itr)
    count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
    return count_reduce

def average(itr):
    # If itr is not iterable, this will generate an iterator.
    iterable = iter(itr)


with open('1kSalesRec.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)
    belgium = None
    print(belgium)
    csvfile.seek(0)
    avg_portugal = None
    print(avg_portugal)
