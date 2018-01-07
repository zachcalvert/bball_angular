import random

def random_item(l):
	size = len(l)
	return l[random.randint(0,size-1)]