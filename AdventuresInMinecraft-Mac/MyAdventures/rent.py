import mcpi.minecraft as minecraft
import time
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

rent = 0
inField = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()

    if pos.x>x1 and pos.x<=x2 and pos.z>=z1 and pos.z<=z2:
        rent = rent+1
        mc.postToChat("You owe rent: "+str(rent))
        inField = inField+1
    else: # not inside the field
        inField = 0

    if inField>3:
        mc.postToChat("Too slow!")
        mc.player.setPos(HOME_X,HOME_Y + 100, HOME_Z)
