import mcpi.minecraft as minecraft #uses minecraft API
mc = minecraft.Minecraft.create() #connection to current game
pos = mc.player.getTilePos()
mc.postToChat("x = " + str(pos.x) + " y = " + str(pos.y) + " z = " + str(pos.z))
