from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

height = [100, 0]
count = 0

while count < 5:
    pos = mc.player.getTilePos()
    
    if pos.y < height[0]:
        height[0] = pos.y
    if pos.y > height[1]:
        height[1] = pos.y
    count += 1
    time.sleep(1)
    
mc.postToChat("Lowest: "  + str(height[0]))
mc.postToChat("Highest: " + str(height[1]))