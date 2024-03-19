import RPi.GPIO as GPIO
import time

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    t = float(input("Введите период сигнала:"))
    while True:
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(t / 512)
        for i in range(256):
            GPIO.output(dac, dec2bin(255 - i))
            time.sleep(t / 512)

finally:
    GPIO.output(dac, 0) 
    GPIO.cleanup()