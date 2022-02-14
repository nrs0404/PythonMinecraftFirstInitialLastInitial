from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

depth = 0
for i in range(49):
    block = mc.getBlock(x, y, z)
    y -= 1
    depth += 1
    
    if block == 56:
        mc.postToChat("There are diamonds " + str(depth) + " blocks down")
    #else:
        #mc.postToChat("There Are No Diamonds")
    #break
        
    
    
    
    
    
     