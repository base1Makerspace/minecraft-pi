import mcpi.block as block
from random import randint

class WallBuilder(object):
	def __init__(self, mc):
		self.mc = mc
	
	def placeWalls(self):
		""" Randomly builds Walls """
		for q in xrange(15):
			x = randint(-25, 25)
			z = randint(-25, 25)
			length = randint(3, 7)

			self.mc.setBlocks(
				x,
				0,
				z,
				x + length,
				2,
				z,
				block.STONE.id
			)

		for q in xrange(15):
			x = randint(-25, 25)
			z = randint(-25, 25)
			length = randint(3, 7)

			self.mc.setBlocks(
				x,
				0,
				z,
				x ,
				2,
				z + length,
				block.STONE.id
			)
