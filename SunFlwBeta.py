plant(Entities.Sunflower)

HEIGHT = 12
WIDTH = 12


def plant_column():
    for _ in range(HEIGHT):
        plant(Entities.Sunflower)
        move(South)


def harvest_column():
    for _ in range(HEIGHT):
        harvest()
        move(North)


def go_to_top():
    for _ in range(HEIGHT):
        move(North)


def delay():
    for _ in range(4):
        print(1)


while True:

    for _ in range(WIDTH):
        plant_column()
        move(West)
    go_to_top()

    delay()

    for _ in range(WIDTH):
        harvest_column()
        move(West)
    go_to_top()