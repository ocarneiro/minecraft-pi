from mcpi import minecraft

FERRO_MINERIO = 15
REDSTONE = 73
AR = 0
PEDRA = 1

def diga_ola():
    mc.postToChat("Ola")  

def cria_palco():
    x,y,z = mc.player.getPos()
    mc.setBlocks(x+1,y,z+1,x+11,y+11,z+11,AR)
    mc.setBlocks(x+1,y-1,z,x+11,y,z+11,PEDRA)
    mc.setBlock(x+4, y+1, z+5, REDSTONE)
    mc.setBlock(x+6, y+1, z+5, FERRO_MINERIO)



mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
#diga_ola()
cria_palco()

bloco_desejado = 1 #pedra

#while True:
#    x,y,z = mc.player.getPos()
#    bloco_abaixo = mc.getBlock(x,y-1,z)
    #verifica se esta em cima de um bloco
#    if bloco_abaixo == bloco_desejado:
#        diga_ola()



