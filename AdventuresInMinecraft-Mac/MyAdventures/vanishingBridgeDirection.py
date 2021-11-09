import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

bridge = []
BLOCKDISTANCE = 1
def buildBridge():
    pos = mc.player.getTilePos()
    direction = mc.player.getDirection()

    x = round(pos.x + (direction.x * BLOCKDISTANCE))
    y = round(pos.y + (direction.y * BLOCKDISTANCE) + 1)
    z = round(pos.z + (direction.z * BLOCKDISTANCE))
    
    b = mc.getBlock(x, pos.y-1, z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(x, pos.y-1, z, block.GLASS.id)
        coordinate = [x, pos.y-1, z]
        bridge.append(coordinate)
    elif b !=block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            time.sleep(0.05)

while True:
    buildBridge()
        
