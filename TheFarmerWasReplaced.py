while True:
	
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	while True:
		substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
		if num_items(Items.Weird_Substance) < substance:
			trade(Items.Weird_Substance, substance)
		use_item(Items.Weird_Substance, substance)
		dirs = [North, East, South, West]
		d = 0
		while not (get_ground_type() == Entities.Treasure or get_entity_type() == Entities.Treasure):
		
			right = (d + 1) % 4
			if move(dirs[right]):
				d = right
			elif move(dirs[d]):
				pass
			else:
				left = (d - 1) % 4
				if move(dirs[left]):
					d = left
				else:
					move(dirs[(d + 2) % 4])
					d = (d + 2) % 4
		harvest()
		break