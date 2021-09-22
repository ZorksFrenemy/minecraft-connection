import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
size = int(input("size of area to clear? "))

mc.setBlocks(pos.x-size/2, pos.y, pos.z-size/2, pos.x+size/2, pos.y+size, pos.z+size/2, block.AIR.id)
