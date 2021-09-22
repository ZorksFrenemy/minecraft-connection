import mcpi.minecraft as minecraft
import mcpi.block as block
import time

#how far in front of the player the block will be
BLOCKDISTANCE = 5

mc = minecraft.Minecraft.create()

while True:
    #get the position
    pos = mc.player.getPos()
    #get the direction
    direction = mc.player.getDirection()
    #calc the position of the block in front of the player
    x = round(pos.x + (direction.x * BLOCKDISTANCE))
    y = round(pos.y + (direction.y * BLOCKDISTANCE) + 1)
    z = round(pos.z + (direction.z * BLOCKDISTANCE))
    mc.setBlock(x,y,z,block.DIAMOND_BLOCK)
    time.sleep(0.1)
    mc.setBlock(x,y,z,block.AIR)
