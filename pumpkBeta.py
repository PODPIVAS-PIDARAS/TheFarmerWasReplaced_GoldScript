def plant_column():
    for _ in range(12):
        plant(Entities.Pumpkin)
        move(South)


def harvest_column():
    for _ in range(12):
        harvest()
        move(North)


def fix_column_once():
    for _ in range(12):

        if get_entity_type() != Entities.Pumpkin or not can_harvest():
            plant(Entities.Pumpkin)
        move(South)


def go_to_top():
    for _ in range(12):
        move(North)


while True:

    for _ in range(12):
        plant_column()
        move(West)
    go_to_top()

    for _ in range(12):
        fix_column_once()
        move(West)
    go_to_top()

    change_hat(Hats.Straw_Hat)
    for _ in range(12):
        harvest_column()
        move(West)
    go_to_top()