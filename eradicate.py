import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from random import randint

# mc = minecraft.Minecraft.create()
mc = minecraft.Minecraft.create('10.0.108.6')

mc.postToChat('Hello it\' me')

blockSize = 50

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

for q in xrange(15):
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


mc.camera.setFixed()
mc.camera.setPos(x, y + 20, z)