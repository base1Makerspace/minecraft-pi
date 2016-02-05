import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

mc = minecraft.Minecraft.create('10.0.108.102')
mc.postToChat("Hello")

pos = mc.player.getTilePos()
#~ X = vu riets lenks,y ass d'heicht, z ass deift
x,y,z = pos
mc.postToChat(x)

x = 5
z = 10

mc.setBlocks(
	x,y,z,
	x + 6,y + 5,z + 2,
	#~ block.STONE.id
	block.WOOL.id,
	4
)


#~ block.WOOD.id
#~ block.STONE.id

