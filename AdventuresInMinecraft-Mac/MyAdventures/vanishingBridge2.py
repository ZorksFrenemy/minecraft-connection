import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

bridge = []

def buildBridge():
    pos = mc.player.getTilePos()
    #b = mc.getBlock(pos.x, pos.y-1, pos.z)

    areaCheck(pos)
    
##    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
##        mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)
##        coordinate = [pos.x, pos.y-1, pos.z]
##        bridge.append(coordinate)
##    elif b !=block.GLASS.id:
##        if len(bridge) > 0:
##            coordinate = bridge.pop()
##            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
##            time.sleep(0.05)


def areaCheck(position):
    b = mc.getBlock(position.x, position.y-1, position.z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id or b == block.GLASS.id:
        mc.setBlock(position.x, position.y-1, position.z, block.GLASS.id)
        coordinate = [position.x, position.y-1, position.z]
        bridge.append(coordinate)
        for a in range(10):
            for c in range(10):
                b = mc.getBlock(position.x-5+a,position.y-1,position.z-5+c)
                
                if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
                    mc.setBlock(position.x-5+a, position.y-1, position.z-5+c, block.GLASS.id)
                    coordinate = [position.x-5+a, position.y-1, position.z-5+c]
                    bridge.append(coordinate)
    elif b !=block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            time.sleep(0.05)

    

while True:
    buildBridge()
        
