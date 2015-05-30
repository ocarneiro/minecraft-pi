from mcpi import minecraft
import time
import RPi.GPIO as GPIO

#pinos
LED_VERDE = 22
LED_VERMELHO = 18
MOTOR = 16

#blocos
FERRO_MINERIO = 15
REDSTONE = 73
AR = 0
PEDRA = 1
DIAMANTE = 56

def prepara_pinos():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_VERDE, GPIO.OUT)
    GPIO.output(LED_VERDE, GPIO.LOW)
    GPIO.setup(LED_VERMELHO, GPIO.OUT)
    GPIO.output(LED_VERMELHO, GPIO.LOW)
    GPIO.setup(MOTOR, GPIO.OUT)
    GPIO.output(MOTOR, GPIO.LOW)

def diga_ola():
    mc.postToChat("Ola")  

def cria_palco():
    mc.player.setPos(0,10,0)
    time.sleep(1.0) #espera personagem cair
    x,y,z = mc.player.getPos()
    mc.setBlocks(x+1,y,z+1,x+11,y+11,z+11,AR)
    mc.setBlocks(x+1,y-1,z,x+11,y,z+11,PEDRA)
    mc.setBlocks(x+3, y+1, z+5, x+3, y+2, z+5, FERRO_MINERIO)
    mc.setBlocks(x+7, y+1, z+5, x+7, y+2, z+5, REDSTONE)
    mc.setBlocks(x+3, y+1, z+10, x+7, y+8, z+10, DIAMANTE)


def acende_verde():
    GPIO.output(LED_VERDE, GPIO.HIGH)
    GPIO.output(LED_VERMELHO, GPIO.LOW)
    time.sleep(1.0)
    GPIO.output(LED_VERDE, GPIO.LOW)

def acende_vermelho():
    GPIO.output(LED_VERDE, GPIO.LOW)
    GPIO.output(LED_VERMELHO, GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(LED_VERMELHO, GPIO.LOW)

def liga_motor():
    GPIO.output(LED_VERDE, GPIO.LOW)
    GPIO.output(LED_VERMELHO, GPIO.LOW)
    GPIO.output(MOTOR, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(MOTOR, GPIO.LOW)


mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
prepara_pinos()
#diga_ola()
cria_palco()

bloco_desejado = 1 #pedra

while True:
    x,y,z = mc.player.getPos()
    bloco_afrente = mc.getBlock(x,y,z+1)
    #verifica se esta em cima de um bloco
    if bloco_afrente == FERRO_MINERIO:
        acende_verde()
    elif bloco_afrente == REDSTONE:
        acende_vermelho()
    elif bloco_afrente == DIAMANTE:
        liga_motor()





