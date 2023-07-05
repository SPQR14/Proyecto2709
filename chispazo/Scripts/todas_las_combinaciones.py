import itertools

comb = itertools.combinations(range(1,29), 5)

for x in list(comb):
    print(x)