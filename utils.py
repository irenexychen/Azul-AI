import random

def random_factory(num_factories):
	return random.randint(0, num_factories)

def random_tile(factory):
	return random.choice(factory)
