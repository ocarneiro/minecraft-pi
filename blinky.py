import time
import RPi.GPIO as GPIO

LED_VERDE = 22
LED_VERMELHO = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.output(LED_VERDE, GPIO.LOW)
GPIO.setup(LED_VERMELHO, GPIO.OUT)
GPIO.output(LED_VERMELHO, GPIO.LOW)

while True:
    GPIO.output(LED_VERDE, GPIO.HIGH)
    GPIO.output(LED_VERMELHO, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LED_VERDE, GPIO.LOW)
    GPIO.output(LED_VERMELHO, GPIO.HIGH)
    time.sleep(0.5)
