change_hat(Hats.Carrot_Hat)

HEIGHT = 12
WIDTH = 12


def plant_column():
    for _ in range(HEIGHT):
        plant(Entities.Carrot)
        move(South)


def harvest_column():
    for _ in range(HEIGHT):
        harvest()
        move(North)


def go_to_top():
    for _ in range(HEIGHT):
        move(North)


while True:

    for _ in range(WIDTH):
        plant_column()
        move(West)
    go_to_top()

    for _ in range(WIDTH):
        harvest_column()
        move(West)
    go_to_top()