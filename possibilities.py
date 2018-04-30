import itertools


def expand(t):
    return expand_rec(t, 0)


def expand_rec(t, i):
    if i == 9:
        return t
    if i + 1 in t:
        return expand_rec(t, i + 1)
    return expand_rec(t[0:i] + (0,) + t[i:], i + 1)


def display(t):
    s = str(t)
    s = s.replace('0', ' ')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace(',', ' ')
    print(s)


def restrict(t, rs):
    outer_valid = True
    for r in rs:
        inner_valid = False
        for z in r:
            if z in t:
                inner_valid = True
                break
        outer_valid = outer_valid and inner_valid
    return outer_valid


target = 28
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 6
#restrictions = ((4, 5), (8, 7))
restrictions = ()

combinations = list(itertools.combinations(digits, count))
for x in combinations:
    if sum(x) == target and restrict(x, restrictions):
        display(expand(x))
