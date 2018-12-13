# Created by mqgao at 2018/12/13

from collections import defaultdict
import re


def get_pixels_by_coor(x, y, width, height):
    for i in range(height):
        for w in range(width):
            yield (x + w, y + i)


def record_pixels_by_coordinations(coordinations):
    all_pixels_with_overlap = defaultdict(set)

    for _id, x, y, width, height in coordinations:
        for px, py in get_pixels_by_coor(x, y, width, height):
            all_pixels_with_overlap[(px, py)].add(_id)

    return all_pixels_with_overlap


def get_pixels_by_pred(all_pixels_with_overlap, pred=lambda x: True):
    return {k: v for k, v in all_pixels_with_overlap.items() if pred(v)}


def get_intact_pixels(all_pixels_with_overlap):
    all_overlapped = set()
    may_intact = set()

    for position, ids in all_pixels_with_overlap.items():
        if len(ids) > 1: all_overlapped |= ids
        if len(ids) == 1: may_intact |= ids

    return may_intact - all_overlapped


pattern = re.compile('#(?P<id>\d+)\s+@\s+(?P<x>\d+),(?P<y>\d+):\s+(?P<width>\d+)x(?P<height>\d+)')


def parse_coordination(coordiantion_str):
    _id, x, y, width, height = pattern.findall(coordiantion_str)[0]

    return int(_id), int(x), int(y), int(width), int(height)


g = get_pixels_by_coor(3, 2, 5, 4)

assert next(g) == (3, 2)
assert next(g) == (4, 2)
assert next(g) == (5, 2)
assert next(g) == (6, 2)
assert next(g) == (7, 2)
assert next(g) == (3, 3)
assert next(g) == (4, 3)
assert next(g) == (5, 3)
assert next(g) == (6, 3)
assert next(g) == (7, 3)
assert next(g) == (3, 4)
assert next(g) == (4, 4)
assert next(g) == (5, 4)
assert next(g) == (6, 4)
assert next(g) == (7, 4)
assert next(g) == (3, 5)
assert next(g) == (4, 5)
assert next(g) == (5, 5)
assert next(g) == (6, 5)
assert next(g) == (7, 5)

assert parse_coordination('#123 @ 3,2: 5x4') == (123, 3, 2, 5, 4)


assert len(get_pixels_by_pred(record_pixels_by_coordinations([
    (1, 1, 3, 4, 4),
    (2, 3, 1, 4, 4),
    (3, 5, 5, 2, 2),
]), pred=lambda x: len(x) > 1)) == 4

assert get_intact_pixels(record_pixels_by_coordinations([
    (1, 1, 3, 4, 4),
    (2, 3, 1, 4, 4),
    (3, 5, 5, 2, 2),
])) == {3}


if __name__ == '__main__':
   strings = [line.strip() for line in open('data/input-day3.txt')]
   coordinations = [parse_coordination(s) for s in strings]
   # print(len(get_pixels_by_pred(record_pixels_by_coordinations(coordinations), pred=lambda x: len(x) > 1)))
   print(get_intact_pixels(record_pixels_by_coordinations(coordinations)))

