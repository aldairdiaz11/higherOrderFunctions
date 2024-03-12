import csv
from functools import reduce


def count(predicate: any, itr: iter) -> int:
    count_filter = filter(predicate, itr)
    count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
    return count_reduce


def average(itr: iter) -> float:
    # If itr is not iterable, this will generate an iterator.
    return avg_helper(0, itr, 0)


def avg_helper(curr_count: int, itr_: iter, curr_sum: int) -> float:
    next_sum = next(itr_, "null")

    if next_sum == "null":
        return curr_sum / curr_count
    curr_sum += next_sum
    curr_count += 1
    return avg_helper(curr_count, itr_, curr_sum)


with open('1kSalesRec.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)
    belgium = count(lambda x: x[1] == "Belgium", reader)
    print(belgium)
    csvfile.seek(0)
    avg_portugal = average(
        map(lambda x: float(x[13]),
            filter(lambda x: x[1] == "Portugal", reader)))
    print(avg_portugal)
