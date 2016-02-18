import mcpi.block as block
from random import randint

class WorldBuilder(object):

	def __init__(self, mc):
		self.mc = mc
		self.undergroundBlocks = [
			block.STONE.id,
			block.STONE.id,
			block.GRAVEL.id,
			block.IRON_ORE.id,
			block.COAL_ORE.id,
			block.GRAVEL.id
		]
		
	def getRandomBlock(self):
		return self.undergroundBlocks[
			randint(0, len(self.undergroundBlocks) - 1)
		]
		
	def flattenMap(self, blockSize):
		""" Flattens the map """
		# Flatten map
		self.mc.setBlocks(
			- blockSize,
			0,
			blockSize,

			blockSize,
			blockSize,
			- blockSize,
			block.AIR.id
		)
		# Set ground
		self.mc.setBlocks(
			- blockSize, # x
			- 1,		# y
			blockSize,	# z
			
			blockSize, #x1
			- 1,	
			- blockSize,
			block.GRASS.id
		)
		
	def buildUnderground(self, blockSize):
		for x in xrange(-blockSize, blockSize, 2):
			for z in xrange(-blockSize, blockSize, 2):
				for y in xrange(2, 8, 2):
					print (x, -y, z)
					self.mc.setBlocks(
						x, -y, z,
						x + 1, -y - 1, z + 1,
						self.getRandomBlock()
					)
