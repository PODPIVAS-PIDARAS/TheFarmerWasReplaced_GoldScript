change_hat(Hats.Tree_Hat)

SIZE = 12


def plant_column():
    for _ in range(SIZE):
        plant(Entities.Bush)
        move(South)


def harvest_column():
    for _ in range(SIZE):
        harvest()
        move(North)


def go_to_top():
    for _ in range(SIZE):
        move(North)


while True:

    for _ in range(SIZE):
        plant_column()
        move(West)

    go_to_top()

    for _ in range(SIZE):
        harvest_column()
        move(West)


