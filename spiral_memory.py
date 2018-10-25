RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, 1)
DOWN = (0, -1)


def move_by_sprial():
    "Yield successive (x, y) coordinates of squares on a spiral."
    x = y = s = 0   # (x, y) is the position; s is the side length.
    yield (x, y)
    while True:
        for (dx, dy) in (RIGHT, UP, LEFT, DOWN):
            if dy: s += 1 # Increment side length before RIGHT and LEFT
            for _ in range(s):
                x += dx; y += dy
                yield (x, y)



def sprial(move_step):
    
    for i, (x, y) in enumerate(move_by_sprial()):
        if i == move_step:
            return x, y

print(sprial(0))
print(sprial(1))
print(sprial(2))
print(sprial(3))

