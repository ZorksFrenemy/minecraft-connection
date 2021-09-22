import mcpi.minecraft as minecraft #uses minecraft API
import time
mc = minecraft.Minecraft.create() #connection to current game

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("x = " + str(pos.x) + " y = " + str(pos.y) + " z = " + str(pos.z))
