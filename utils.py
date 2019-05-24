import random

def random_factory(factory_index):
	return random.choice(factory_index)

def random_tile(factory):
	return random.choice(factory)

def random_row(num_rows):
	return random.randint(0, num_rows - 1)
