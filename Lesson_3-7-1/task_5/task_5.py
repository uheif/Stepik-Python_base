from functools import reduce

with open("dataset_3380_5.txt") as inf:
    lst = [line.strip('\n').split('\t') for line in inf]

clses = {i: reduce(lambda stk, el: stk + [int(el[2])] if el[0] == str(i) else stk, lst, []) for i in range(1, 12)}

for key, value in clses.items():
    print(key, sum(value) / len(value)) if value else print(f"{key} -")