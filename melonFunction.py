from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time
count = 0
def makeMelon():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    randx = random.randint(-5, 5)
    randz = random.randint(-5, 5)
    mc.setBlock(x + randx, y - 1, z + randz, 103)
    time.sleep(2)

while count < 6:
    makeMelon()
    count += 1