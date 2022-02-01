from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

for i in range(49):
    block = mc.getBlock(x, y, z)
    y -= 1

    
    if block == 56:
        mc.postToChat("You got a Diamond!")
    else:
        mc.postToChat("There Are No Diamonds")
    break
        
    
    
    
    
    
     