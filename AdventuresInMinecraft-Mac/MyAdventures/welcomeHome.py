import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
home = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()

   
    if pos.x == 157 and pos.z == 158:
        if home == 0:
            mc.postToChat("welcome home")
            home = home + 1
    else:
        home = 0
