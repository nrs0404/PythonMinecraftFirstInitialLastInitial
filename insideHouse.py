from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX =53
buildY =23
buildZ =22
width = 11
height = 6
length = 7

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length

mc.postToChat("You are inside: " + str(inside))