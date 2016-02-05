import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

mc = minecraft.Minecraft.create('10.0.108.6')

mc.setBlocks(
	0,0,0,
	50,20,50,
	block.DIAMOND_BLOCK.id
)

mc.player.setPos(0,21,0)
