import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

DIEDISTANCE = 15


def one(x,y,z):
    mc.setBlock((x,y+3,z),block.BEDROCK)
    
def two(x,y,z):
    mc.setBlock((x-2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3-2,z),block.BEDROCK)
    
def three(x,y,z):
    mc.setBlock((x-2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3-2,z),block.BEDROCK)
    mc.setBlock((x,y+3,z),block.BEDROCK)
    
def four(x,y,z):
    mc.setBlock((x-2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3-2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x-2,y+3-2,z),block.BEDROCK)
    
def five(x,y,z):
    mc.setBlock((x-2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3-2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x-2,y+3-2,z),block.BEDROCK)
    mc.setBlock((x,y+3,z),block.BEDROCK)
 
def six(x,y,z):
    mc.setBlock((x-2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3-2,z),block.BEDROCK)
    mc.setBlock((x+2,y+3+2,z),block.BEDROCK)
    mc.setBlock((x-2,y+3-2,z),block.BEDROCK)
    mc.setBlock((x-2,y+3,z),block.BEDROCK)
    mc.setBlock((x+2,y+3,z),block.BEDROCK)
    
def die():
    a=1


def roll(x,y,z):
    die = [one, two, three, four, five, six]
    random.choice(die)(x,y,z)
    #six(x,y,z)
    

def getCenter():
    pos = mc.player.getPos()
    direction = mc.player.getDirection()
    x = round(pos.x + (direction.x * DIEDISTANCE))
    y = round(pos.y + (direction.y * DIEDISTANCE) + 1)
    z = round(pos.z + (direction.z * DIEDISTANCE))
    return x,y,z


x,y,z = getCenter()

for a in range(70):
    
    time.sleep(0.05)
    #mc.setBlocks(x-3,y,z,x+3,y+6,z,block.AIR)
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.GLOWSTONE_BLOCK)
    time.sleep(0.02)
    roll(x,y,z)


for a in range(20):
    
    time.sleep(0.1)
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.AIR)
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.GLOWSTONE_BLOCK)
    time.sleep(0.04)
    roll(x,y,z)

for a in range(10):
    
    time.sleep(0.2)
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.AIR)
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.GLOWSTONE_BLOCK)
    time.sleep(0.06)
    roll(x,y,z)

mc.setBlocks(x-3,y,z,x+3,y+6,z,block.AIR)
