import mcpi.minecraft as minecraft
import mcpi.block as block
import time, sys
from random import randint
mc = minecraft.Minecraft.create('10.0.107.48')

if __name__ == "__main__":
	while True:
		 blockEvents = mc.events.pollBlockHits()
		 print(blockEvents)
		 if blockEvents != []:	
			blockevent = blockEvents[0]
			print(blockevent.pos)
			x, y, z = blockevent.pos
			mc.setBlocks(x + 3, y, z + 1, x - 2, y + 4, z + 7, block.BRICK_BLOCK)
			time.sleep(0.5)
			mc.setBlocks(x, y + 1, z + 1, x + 1, y + 2, z + 1, block.AIR)
			time.sleep(0.5)
			mc.setBlocks(x + 2, y + 1, z + 2, x - 1, y + 3, z + 6, block.AIR)
			time.sleep(0.5)
			mc.setBlocks(x - 2, y + 2, z + 3, x - 2, y + 3, z + 5, block.GLASS_PANE)
			mc.setBlocks(x + 3, y + 2, z + 3, x + 3, y + 3, z + 5, block.GLASS_PANE)
			time.sleep(0.5)
			mc.setBlocks(x + 2, y, z + 2, x - 1, y, z + 6, block.WOOD_PLANKS)
			time.sleep(0.5)
			mc.setBlock(x + 2, y + 2, z + 2, block.TORCH.id, 2)
			mc.setBlock(x + 2, y + 2, z + 6, block.TORCH.id, 2)
			mc.setBlock(x - 1, y + 2, z + 2, block.TORCH.id, 1)
			mc.setBlock(x - 1, y + 2, z + 6, block.TORCH.id, 1)
			time.sleep(0.5)
			mc.setBlock(x + 1, y + 1, z + 6, block.FURNACE_ACTIVE)
			mc.setBlock(x + 2, y + 1, z + 6, block.CRAFTING_TABLE)
			mc.setBlock(x - 1, y + 1, z + 6, block.CHEST)
			time.sleep(0.5)
			mc.setBlocks(x + 4, y + 5, z, x - 3, y + 5, z + 8, block.STONE_SLAB)
			time.sleep(0.5)
			mc.setBlocks(x + 3, y + 5, z + 1, x - 2, y + 5, z + 7, block.STONE_SLAB_DOUBLE)
			time.sleep(0.5)
			mc.setBlocks(x + 2, y + 6, z + 2, x - 1, y + 6, z + 6, block.STONE_SLAB)
			time.sleep(0.5)
			mc.setBlocks(x + 1, y + 6, z + 3, x, y + 6, z + 5, block.STONE_SLAB_DOUBLE)
			time.sleep(0.5)
			mc.setBlocks(x, y, z, x + 1, y, z - 6, block.STONE_SLAB_DOUBLE)
			mc.setBlocks(x, y + 3, z, x + 1, y + 1, z - 6, block.AIR)
			
			#~ event, x, y, z, face, entity = blockevent
			#~ print(event)
		 time.sleep(0.2)
