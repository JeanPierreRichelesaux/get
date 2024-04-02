import RPi.GPIO as GPIO
import time

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            return i
    return 256

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        value = adc()
        print("V =", round(int(value) / 256 * 330)/100, value, "В", end = " ")
        for x in dec2bin(value):
            print(x, end = "")
        print()

        
except KeyboardInterrupt:
    time.sleep(0)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()