import itertools
import sys


def expand(t):
    return expand_rec(t, 0)


def expand_rec(t, i):
    if i == 9:
        return t
    if i + 1 in t:
        return expand_rec(t, i + 1)
    return expand_rec(t[0:i] + (0,) + t[i:], i + 1)


def get_friendly(t):
    s = str(t)
    s = s.replace('0', ' ')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace(',', ' ')
    return s


def one_of_each(t, sr):
    outer_valid = True
    for r in sr:
        inner_valid = False
        for z in r:
            if z in t:
                inner_valid = True
                break
        outer_valid = outer_valid and inner_valid
    return outer_valid


def all_of_any(t,hr):
    for r in hr:
        inner_valid = True
        for z in r:
            inner_valid = inner_valid and z in t
        if inner_valid:
            return True
    return False


def calculate(target, count, soft_restrictions=(), hard_restrictions=()):
    result = ""
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combinations = list(itertools.combinations(digits, count))
    for x in combinations:
        if sum(x) == target and one_of_each(x, soft_restrictions) and all_of_any(x, hard_restrictions):
            result = result + get_friendly(expand(x)) + "\r\n"
    return result[0:len(result)-2]


target = 34
count = 6
if len(sys.argv) == 2:
    target = int(sys.argv[1])
    count = int(sys.argv[2])

one = ((2, 3, 4, 5),)
all = ()
all = ((5, 9), (6, 8))

x = calculate (target, count, one, all)
print(x)