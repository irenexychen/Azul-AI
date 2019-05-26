import random

def random_factory(factory_index):
	return random.choice(factory_index)

def random_tile(factory):
	return random.choice(factory)

def random_row(available_rows):
	return random.choice(available_rows)
