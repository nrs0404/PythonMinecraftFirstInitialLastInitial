from mcpi.minecraft import Minecraft
mc = Minecraft.create()

toDoList = open("/home/pi/PythonMinecraftNS/toDoList.txt", "r")

for line in toDoList:
    mc.postToChat(toDoList.readline(range(0, 8)) 