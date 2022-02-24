from mcpi.minecraft import Minecraft
mc = Minecraft.create() 

secretFile = open("secretFile.txt" , "r")

print(secretFile.read())
secretFile.close()