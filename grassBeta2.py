while True:
	for direction in [North, East, South, West]:
		harvest()
		move(direction)