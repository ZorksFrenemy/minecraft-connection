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


def roll():
    x,y,z = getCenter()
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.GLOWSTONE_BLOCK)
    die = [one, two, three, four, five, six]
    random.choice(die)(x,y,z)
    #six(x,y,z)
    time.sleep(0.2)
    mc.setBlocks(x-3,y,z,x+3,y+6,z,block.AIR)
    
    

def getCenter():
    pos = mc.player.getPos()
    direction = mc.player.getDirection()
    x = round(pos.x + (direction.x * DIEDISTANCE))
    y = round(pos.y + (direction.y * DIEDISTANCE) + 1)
    z = round(pos.z + (direction.z * DIEDISTANCE))
    return x,y,z

while True:
    roll()
