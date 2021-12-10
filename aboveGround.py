from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
mc.postToChat(highestBlockY)
if y >= highestBlockY:
    mc.postToChat("You are above ground")
else:
    mc.postToChat("You are below ground")
    
    