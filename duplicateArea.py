from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2
    
    
def copyStructure(x1 , y1, z1, x2, y2, z2):
    
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)
    
    width = x2 - x1
    height = y2 - y1
    length = z2 - z1
    
    structure = []
    
    print("Please wait...")
    
    for z in range(z1, z2 + 1):
        wall = []
        for x in range(x1, x2 + 1):
            stack = []
            for y in range(y1, y2 + 1):
                block = mc.getBlock(x ,y ,z)
                stack.append(block)
            wall.append(stack)
        structure.append(wall)
    print(structure)

    
    return structure

def buildStructure(x, y, z, structure):
    xStart = x
    yStart = y
    for wall in structure:
        for stack in wall:
            for block in stack:
                mc.setBlock(x, y, z, block)
                y += 1
            y = yStart
            x += 1
        x = xStart
        z += 1
                
    
    
    
    
input("Move to the first corner and press enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z
    
input("Move to the opposite corner and press enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z
    
structure = copyStructure(x1, y1, z1, x2, y2, z2)
    
input("Move to the position you want to create the structure and preess Enter in this window")
    
pos = mc.player.getTilePos()
x , y, z = pos.x, pos.y, pos.z
buildStructure(x, y, z, structure)