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

    x2 = round(pos.x + (direction.x * BLOCKDISTANCE*2))
    y2 = round(pos.y + (direction.y * BLOCKDISTANCE*2) + 1)
    z2 = round(pos.z + (direction.z * BLOCKDISTANCE*2))
    
    b = mc.getBlock(x, pos.y-1, z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(x, pos.y-1, z, block.GLASS.id)
        
        coordinate = [x, pos.y-1, z]
        bridge.append(coordinate)
        
        mc.setBlock(x2, pos.y-1, z2, block.GLASS.id)
        
        coordinate = [x2, pos.y-1, z2]
        bridge.append(coordinate)
    elif b !=block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            time.sleep(0.01)

while True:
    buildBridge()
        
