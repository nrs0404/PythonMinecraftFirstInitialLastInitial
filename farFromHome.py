from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math
homeX = 10
homeZ = 10
pos = mc.player.getTilePos()
x = pos.x
z = pos.z
distance = math.sqrt((homeX - x) ** 2 + (homeZ - z) ** 2)
mc.postToChat(distance)
mc.postToChat("Your house is nearby:", str(distance))
