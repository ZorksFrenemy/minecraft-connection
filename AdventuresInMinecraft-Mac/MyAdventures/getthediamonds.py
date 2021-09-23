import mcpi.minecraft as minecraft
import time
import random
import mcpi.block as block
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

size = 10
offset = size/2

x1 = pos.x - offset
z1 = pos.z - offset + 9

x2 = pos.x + offset
z2 = pos.z + offset + 9

HOME_X = pos.x
HOME_Z = pos.z
HOME_Y = pos.y

print(x1,z1,x2,z2)

home = 0
inField = 0

while True:
    time.sleep(1)
    limit = 5
    
    try:
        air
    except NameError:
        air = 0


    pos2 = mc.player.getTilePos()
    #if air == 0:
     #   for x in range(int(x1+1),int(x2+1)):
      #      for z in range(int(z1),int(z2+1)):
       #         mc.setBlock(x,HOME_Y,z,block.AIR.id)
        #air = 1
   
    if pos2.x == pos.x and pos2.z == pos.z and pos2.y == pos.y:
        if home == 0:
            mc.postToChat("get the diamonds in 5 seconds or less")
            
            
            for x in range(int(x1+0),int(x2+2)):
                for z in range(int(z1-1),int(z2+2)):
                    mc.setBlock(x,HOME_Y-1,z,block.GLOWSTONE_BLOCK.id)
                    
          
                    
            for x in range(int(x1+0),int(x2+2)):
                for z in range(int(z1-1),int(z2+2)):
                    mc.setBlock(x,HOME_Y,z,block.AIR.id)
                    
        
                    
            for x in range(int(x1+1),int(x2+1)):
                for z in range(int(z1),int(z2+1)):
                    mc.setBlock(x,HOME_Y-1,z,block.BEDROCK.id)
                    
            mc.setBlock(HOME_X,HOME_Y-1,HOME_Z,block.TNT.id)    
            
            home = home + 1
            for blocks in range(10):
                mc.setBlock(HOME_X+random.randint(-4,5), HOME_Y, HOME_Z+random.randint(4,14), block.DIAMOND_BLOCK.id)
    else:
        home = 0

    


    

    


    #for x in range(int(x1+1),int(x2+1)):
     #   for z in range(int(z1),int(z2+1)):
      #      mc.setBlock(x,HOME_Y,z,block.GLOWING_OBSIDIAN.id)

    if pos2.x>x1 and pos2.x<=x2 and pos2.z>=z1 and pos2.z<=z2:
        mc.postToChat(str(limit - inField) + " Seconds Left")
        inField = inField+1
    else: # not inside the field
        inField = 0

    if inField>limit:
        mc.postToChat("Too slow!")
        mc.player.setPos(HOME_X,HOME_Y + 100, HOME_Z)
        
