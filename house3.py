import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

mc = minecraft.Minecraft.create('10.0.108.102')

def buildHouse(pos, width, height, depth):
	buildCube(pos, width, height, depth)
	hollowCube(pos, width, height, depth)
	replaceCorners(pos, width, height, depth)
	buildCeiling(pos, width, height, depth)
	
def buildCube(from_pos, width, height, depth):
	x, y, z = from_pos
	#~ print(from_pos)
	#~ print(x + width, y + height, z + depth)
	mc.setBlocks(
		from_pos,
		x + width, y + height, z + depth,
		block.COBBLESTONE.id
	)
	
def hollowCube(pos, width, height, depth):
	x, y, z = pos
	#~ print(x + 1, y, z + 1)
	#~ print(x + (width - 1), y + (height - 1), z + (depth - 1))
	mc.setBlocks(
		x + 1, y, z + 1,
		x + (width - 1), y + (height), z + (depth - 1),
		block.AIR.id
	)

def replaceCorners(pos, width, height, depth):
	x, y, z = pos
	for corner in [(x,z), (x + width, z), (x, z + depth), (x + width, z + depth)]:
		x, z = corner
		time.sleep(1)
		mc.setBlocks(
			x, y, z,
			x, y + 2, z,
			block.WOOD.id
		)
	
def buildCeiling(pos, width, height, depth):
	x, y, z = pos
	mc.setBlocks(
		x + width, y + (height + 1), z + depth,
		x, y + (height + 1), z,
		108,
		2	# defines orientation
	)
	
		
	
if __name__ == "__main__":
	mc.postToChat("Dein Haus wird gebaut")
	mc.postToChat("5")
	time.sleep(1)
	mc.postToChat("4")
	time.sleep(1)
	mc.postToChat("3")
	time.sleep(1)
	mc.postToChat("2")
	time.sleep(1)
	mc.postToChat("1")
	time.sleep(1)
	player = mc.player.getTilePos()
	mc.postToChat(player)
	x, y, z = player
	pos = minecraft.Vec3(x + 5, y, z + 5)
	buildHouse(pos, 5, 2, 6)


  
