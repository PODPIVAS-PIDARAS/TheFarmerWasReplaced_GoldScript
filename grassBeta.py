while True:
	set_world_size(3)
	for direction in [North, East, South, West]:
		harvest()
		move(direction)