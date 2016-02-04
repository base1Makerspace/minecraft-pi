import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create('10.0.108.6')


#~ mc.setBlock(pos, block.STONE.id)



def buildHouse(pos, width, height, blocktype):
	x, y, z = pos
	a = x+width
	b = y+ height
	c = z
	mc.setBlocks(
		x, y, z,
		a, b, c,
		blocktype
	)
	
	x, y, z = pos
	a= x
	b=y+height
	c=z+width*2
	mc.setBlocks(
		x, y, z,
		a, b, c,
		blocktype
	)
	z= z+width *2
	a= x+width
	b=y+height
	c=z
	mc.setBlocks(
		x, y, z,
		a, b, c,
		blocktype
	)
	x= x+width
	a=x
	b=y+height
	c=z-width*2
	mc.setBlocks(
		x, y, z,
		a, b, c,
		blocktype
	)
	x, y, z = pos
	a=x+width
	b=y 
	c=z+width*2
	mc.setBlocks(
		x, y, z,
		a, b, c,
		blocktype
		)
	x, y, z = pos
	y = y+height
	a=x+width
	b=y
	c=z+width*2
	mc.setBlocks(
		x, y, z,
		a, b, c,
		blocktype
		)
	x, y, z = pos
	x = x +width/2
	a = x
	y=y+1
	b = y +1
	c=z
	#~ mc.setBlock(
		#~ a, b , c,
		#~ block.AIR.id
		#~ )
	#~ mc.setBlock(
		#~ x, y, z,
		#~ block.DOOR_WOOD.id
	#~ )
	mc.setBlocks(
		x,y,z,
		a,b,c,
		block.DOOR_WOOD.id
	)
 

	
#~ pos = minecraft.Vec3(-22, 10, 00)
pos = mc.player.getTilePos()
buildHouse(pos, 10, 10, block.IRON_BLOCK.id)
time.sleep(5)
#~ pos = minecraft.Vec3(-22, 10, 00)
#~ buildWall2(pos, 20)


	
