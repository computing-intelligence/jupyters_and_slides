__author__ = 'mqgao'
__date__  = '2018.Sept.30'

RIGHT, LEFT, UP, DOWN = (1, 0), (-1, 0), (0, 1), (0, -1)


def move_by_direction(x, y, direction, side):
    dx, dy = direction

    coordination = []

    for _ in range(side):
        x += dx; y += dy
        coordination.append((x, y))

    return coordination


def move_by_sprial(total_step=0):
    x = y = 0  # start place is (0, 0)
    side = 0
    coordination = [(x, y)]  # add initial place to coordination

    while len(coordination) <= total_step:
        for direction in (RIGHT, UP, LEFT, DOWN):
            if direction in (LEFT, RIGHT): side += 1
            coordination += move_by_direction(x, y, direction, side)
            x, y = coordination[-1]  # use the last coordination as beginning (x, y)

    return coordination


def block_distance(x, y): return abs(x) + abs(y)


def get_sprial_distance(steps): return block_distance(*move_by_sprial(steps)[steps-1])


def draw_sprial(steps):
    """
    Draws a sprial memory, e.g
    17	16	15	14	13
    18	5	4	3	12
    19	6	1	2	11
    20	7	8	9	10
    21
    """
    coordination = list(enumerate(move_by_sprial(steps)))  # change [(0, 0), (1, 0), ..] to [(0, (0, 0), (1, (1, 0)))]

    def sort_from_left_upper_to_right_down(index_x_y): return index_x_y[1][1], -index_x_y[1][0]
    # this function is cascade sort, ref: https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes

    coordination = sorted(coordination, key=sort_from_left_upper_to_right_down, reverse=True)

    previous_x, previous_y = coordination[0]

    for i, (x, y) in coordination:
        if y != previous_y: print('')
        print(str(i+1) + '\t'*(steps//1000+1), end='')
        previous_x, previous_y = x, y


assert move_by_direction(0, 0, RIGHT, 1) == [(1, 0)]
assert move_by_direction(0, 0, RIGHT, 2) == [(1, 0), (2, 0)]
assert move_by_direction(1, 1, UP, 1) == [(1, 2)]

assert get_sprial_distance(1) == 0
assert get_sprial_distance(12) == 3
assert get_sprial_distance(23) == 2
assert get_sprial_distance(1024) == 31

draw_sprial(10)
print('*'*8)
draw_sprial(100)
print('*'*8)
draw_sprial(1000)
