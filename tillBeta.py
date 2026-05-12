HEIGHT = 12
WIDTH  = 12

def till_column():
	for _ in range(HEIGHT):
		till()
		move(South)

while True:
	for _ in range(WIDTH):
		till_column()
		move(West)