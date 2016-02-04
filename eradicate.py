import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

# mc = minecraft.Minecraft.create()
mc = minecraft.Minecraft.create('10.0.108.6')
tntBlocks = []
undergroundBlocks = [
	block.STONE.id,
	block.GRAVEL.id,
	block.IRON_ORE.id,
	block.COAL_ORE.id
]


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
		- blockSize, # x
		- 1,		# y
		blockSize,	# z
		
		blockSize, #x1
		- 1,	
		- blockSize,
		block.GRASS.id
	)
	
	# set underground
	# in a later version, try to randomize each individual block 
	# (must use setBlock() and calculate possible block positions 
	# ourselves)
	mc.setBlocks(
		- blockSize, # x
		- 5,		# y
		blockSize,	# z
		
		blockSize, #x1
		- 2,	
		- blockSize,
		undergroundBlocks[randint(0, len(undergroundBlocks) - 1)]
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

def setTNT(number, radius):
	""" Randomly sets a number of TNT """
	for q in xrange(number):
		x = randint(radius * -1, radius)
		z = randint(radius * -1, radius)
		y = -1
		mc.setBlock(
			x,
			y,
			z,
			block.TNT.id,
			0
		)
		pos = minecraft.Vec3(x, y, z)
		tntBlocks.append(pos)
		
def createSphere(blastRadius, pos):
	""" Create sphere of air """
	mc.postToChat("You're too late, the bomb exploded!")
	for x in range(blastRadius * -1, blastRadius):
		for y in range(blastRadius * -1, blastRadius):
			for z in range(blastRadius * -1, blastRadius):
				if x ** 2 + y ** 2 + z ** 2 < blastRadius ** 2:
					mc.setBlock(pos.x + x, pos.y + y, pos.z + z, block.AIR)

# See http://www.stuffaboutcode.com/2013/05/raspberry-pi-minecraft-block-events.html 
def fuseTNT(pos, second):
	for fuse in range(0, second):
		if mc.player.getTilePos() == minecraft.Vec3(pos.x, pos.y + 1, pos.z):
			mc.postToChat("Bomb defused")
			return False 
		mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
		time.sleep(0.5)
		mc.setBlock(pos.x, pos.y, pos.z, block.TNT)
		time.sleep(0.5)   
	return True

#~ def buildTower(height, width):
	#~ mc.setBlocks(
		#~ 1,1,1,
		#~ width,height,2,
		#~ block.WOOD.id
	#~ )
		

if __name__ == "__main__":
	flattenMap(60)
	placeWalls()
	setTNT(20, 15)	# number
	mc.camera.setNormal()
	#~ buildTower(30, 8)
	mc.postToChat("Hello")
	mc.postToChat("Walk over the bombs before they explode.")
	mc.postToChat("Let's start!")
	for tnt in tntBlocks:
		if fuseTNT(tnt, 15):
			createSphere(
				randint(3, 4), 
				tnt
			)
	mc.postToChat ("Game Over!")

