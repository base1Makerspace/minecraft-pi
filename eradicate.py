import mcpi.minecraft as minecraft
import mcpi.block as block
import time, sys
from worldbuilder import WorldBuilder
from wallbuilder import WallBuilder
from random import randint

# mc = minecraft.Minecraft.create()
mc = minecraft.Minecraft.create('10.0.108.6')
wb = WorldBuilder(mc)
wab = WallBuilder(mc)

tntBlocks = []
mc.player.setPos(0,0,0)

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
		if (fuse % 5) == 0:
			mc.postToChat("countdown: %d " % (second - fuse))
		posBlock = minecraft.Vec3(pos.x, pos.y + 1, pos.z)
		posAir = minecraft.Vec3(pos.x, pos.y, pos.z)
		posPlayer = mc.player.getTilePos()
		if posPlayer == posBlock or posPlayer == posAir:
			mc.postToChat("Bomb defused")
			return False 
		mc.setBlock(pos.x, pos.y, pos.z, block.AIR)
		time.sleep(0.5)
		mc.setBlock(pos.x, pos.y, pos.z, block.TNT)
		time.sleep(0.5)   
	return True

lev = 1

if __name__ == "__main__":
	wb.flattenMap(60)
	wb.buildUnderground(60)
	mc.camera.setNormal()
	mc.postToChat("Walk over the bombs before they explode.")
	while True:
		wab.placeWalls(lev)
		mc.postToChat('Level %d' % lev)
		print('Level %d' % lev)
		setTNT(lev * 5, 20 / lev)	# number
		mc.postToChat("Begin!")
		for tnt in tntBlocks:
			if fuseTNT(tnt, 15):
				createSphere(
					randint(4, 5), 
					tnt
				)
				mc.postToChat ("You lose, too bad")
				sys.exit(0)
		mc.postToChat ("Well done!")
		lev = lev + 1
		

