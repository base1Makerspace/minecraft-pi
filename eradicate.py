import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

# mc = minecraft.Minecraft.create()
mc = minecraft.Minecraft.create('10.0.108.6')
tntBlocks = []

mc.postToChat('Hello it\' me')

def flattenMap(blockSize):
	""" Flattens the map """
	# Flatten map
	mc.setBlocks(
		- blockSize,
		0,
		blockSize,

		blockSize,
		blockSize,
		- blockSize,
		block.AIR.id
	)
	# Set ground
	mc.setBlocks(
		- blockSize,
		- 1,
		blockSize,

		blockSize,
		- 1,
		- blockSize,
		block.GRASS.id
	)

mc.player.setPos(0,0,0)

# Todo: Maueren wierklech glaeichmaesseg verdeelen
def placeWalls():
	""" Randomly builds Walls """
	for q in xrange(15):
		x = randint(-25, 25)
		z = randint(-25, 25)
		length = randint(3, 7)

		mc.setBlocks(
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

		mc.setBlocks(
			x,
			0,
			z,
			x ,
			2,
			z + length,
			block.STONE.id
		)

def setTNT(number):
	""" Randomly sets a number of TNT """
	for q in xrange(number):
		x = randint(-25, 25)
		z = randint(-25, 25)
		y = -1
		mc.setBlock(
			x,
			y,
			z,
			block.TNT.id,
			1
		)
		pos = minecraft.Vec3(x, y, z)
		tntBlocks.append(pos)
		#~ print(tntBlocks)

	     
def fuseTNT(pos, second):
	for fuse in range(0, second):
		mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
		time.sleep(0.5)
		mc.setBlock(pos.x, pos.y, pos.z, block.TNT)
		time.sleep(0.5)   

if __name__ == "__main__":
	flattenMap(60)
	placeWalls()
	setTNT(40)
	mc.camera.setNormal()
	playerpos = mc.player.getTilePos()
	for tnt in tntBlocks:
		fuseTNT(tnt, 5)
	

#~ mc.camera.setFixed()
#~ mc.camera.setPos(x, y + 35, z)
#~ 
#~ mc.camera.setFollow()
