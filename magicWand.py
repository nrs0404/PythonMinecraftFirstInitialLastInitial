from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(10)

hits = mc.events.pollBlockHits()
block = 103

for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.setBlocks(x, y, z, block)