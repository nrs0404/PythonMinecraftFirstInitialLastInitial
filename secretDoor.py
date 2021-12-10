from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -10.5
y = 35
z = 5.5
x2 = -8
y2 = 34
z2 = 8

gift = mc.getBlock(x, y, z)
if gift == 57:
    mc.setBlocks(x2, y2 ,z2 ,x2 ,y2 +1,z2, 0)
    mc.postToChat("Thanks Bruh here the secret passage YO")
else:
    mc.postToChat("Place and offering on the pedestal.")
    