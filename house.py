import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

mc = minecraft.Minecraft.create('10.0.108.6')

def buildHouse(start, width, height):
	buildWall(start, "North", width, height)
	buildWall(start, "East", width, height)
	buildWall(start, "West", width, height)
	buildWall(start, "South", width, height)
	buildWall(start, "ceiling", width, height)
	
	
def buildWall(start, direction, width, height):
	#~ print(start, direction, width)
	x, y, z = start
	b = y + height
	
	if direction == "East":
		a = x + width
		c = z
		torch = minecraft.Vec3(x + width / 2, 3, z + 1)
	elif direction == "North":
		a = x
		c = z + width
		torch = minecraft.Vec3(0,0,0) # needs fixing
	elif direction == "West":
		x = x + width
		a = x
		c = z + width
		torch = minecraft.Vec3(0,0,0)	# needs fixing
	elif direction == "South":
		z = z + width
		a = x + width
		c = z
		torch = minecraft.Vec3(x + width / 2, 3, c - 1)
	elif direction == "ceiling":
		x = x
		a = x + width
		c = z + width
		y = height
		b = y

	mc.setBlocks(
		x, y, z,
		a, b, c,
		block.WOOD_PLANKS.id
	)
	
	if direction != "ceiling":
		print(torch)
		mc.setBlock(torch, block.TORCH.id)
	
if __name__ == "__main__":
	player = mc.player.getTilePos()
	start = minecraft.Vec3(0,0,0)
	buildHouse(start, 5, 20)
	mc.player.setPos(3, 0, 3)
