import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

score = 0
RANGE = 5


treasure_x = None # the x-coordinate of the treasure
treasure_y = None
treasure_z = None

def placeTreasure():
    global treasure_x, treasure_y, treasure_z
    pos = mc.player.getTilePos()

    treasure_x = random.randint(pos.x, pos.x+RANGE)
    treasure_y = random.randint(pos.y+2, pos.y+RANGE)
    treasure_z = random.randint(pos.z, pos.z+RANGE)
    mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)


def checkHit ():
    global score
    global treasure_x

    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == treasure_x and pos.y == treasure_y and pos.z == treasure_z:
            mc.postToChat("HIT!")
            score = score + 10
            mc.setBlock(treasure_x,treasure_y, treasure_z, block.AIR.id)
            treasure_x, None





def homingBeacon():
    global timer
    if treasure_x !=None:
        timer = timer - 1
        if timer == 0:
            timer = TIMEOUT
            pos = mc.player.getTilePos()
            diffx = abs(pos.x - treasure_x)
            diffy = abs(pos.y - treasure_y)
            diffz = abs(pos.z - treasure_z)
            diff = diffx + diffy + diffz
            mc.postToChat("score:" + str(score) + "treasure:" + str(diff))
                

bridge = []

def buildBridge():
    print("buildBridge")

while True:
    time.sleep(1)

    if treasure_x == None and len(bridge) == 0:
        placeTreasure()

    checkHit()
    TIMEOUT = 1
    timer = TIMEOUT
    homingBeacon()
    buildBridge()
