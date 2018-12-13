from itertools import repeat


def accumulated_fre(fres): return sum(fres)


def get_first_repeat(fres):
    accumulated = 0

    adjusted = {accumulated}

    for Ns in repeat(fres):
        for n in Ns:
            accumulated += n
            if accumulated not in adjusted: adjusted.add(accumulated)
            else: return accumulated


assert accumulated_fre([0, 1, 2]) == 3
assert accumulated_fre([0, -1, 1]) == 0

assert get_first_repeat([+1, -1]) == 0
assert get_first_repeat([+3, +3, +4, -2, -4]) == 10
assert get_first_repeat([-6, +3, +8, +5, -6]) == 5
assert get_first_repeat([+7, +7, -2, -7, -4]) == 14


if __name__ == '__main__':
    numbers = [int(line.strip()) for line in open('data/input-day1.txt')]
    print(accumulated_fre(numbers))
    print(get_first_repeat(numbers))

