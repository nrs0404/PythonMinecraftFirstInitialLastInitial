from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

count = 0

def growTree(x, y, z):
    mc.setBlocks(x, y, z, x , y + 4, z, 17)
    mc.setBlocks(x-2, y + 5, z-2, x + 2, y + 6, z+ 2, 18)
    mc.setBlocks(x-1, y + 6, z -1, x + 1, y + 7, z + 1, 18)
    mc.setBlocks(x, y + 8, z, x , y + 8, z,18 )
    

while count < 9:
    growTree(x + 1, y, z)
    count += 1
    growTree(x + 7, y , z)
    count += 1
    growTree(x + 13, y, z)
    count += 1
    growTree(x + 19, y, z)
    count += 1
    growTree(x + 25, y, z)
    count += 1
    growTree(x + 31, y, z)
    count += 1
    growTree(x + 37, y, z)
    count += 1
    growTree(x + 43, y, z)
    count += 1
    growTree(x + 49, y, z)
    count += 1