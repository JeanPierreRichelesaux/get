import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
light = [0] * 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def volume():
    value = 0
    signals = [0] * 8
    for i in range(8):
        signals[i] = 1
        GPIO.output(dac, signals)
        time.sleep(0.005)
        if GPIO.input(comp) == 1:
            signals[i] = 0
        else:
            value += 2**(7-i)
    return value

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def shine(val):
    GPIO.output(leds, dec2bin(val))

try:
    data = []
    t0 = time.time()
    GPIO.output(troyka, GPIO.HIGH)
    while True:
        v = volume()
        print(v)
        shine(v)
        if v > 242:
            break
        data.append(v / 255 * 3.3)
    GPIO.output(troyka, GPIO.LOW)
    while True:
        v = volume()
        print(v)
        shine(v)
        if v < 25:
            break
        data.append(v / 255 * 3.3)
    t = time.time()
    texp = t - t0

    c, d = texp / len(data), 3.3 / 255
    plt.plot([x * c for x in range(len(data))], data)
    plt.show()
    print("Общее время:", texp)
    print("Период одного измерения:", texp / 2)
    print("Частота дискретизации:", 1 / c)
    print("Шаг квантования:", d)
    datax = [str(x) for x in data]
    with open("data.txt", "w") as f:
        f.write("\n".join(datax))
    with open("settings.txt", "w") as f:
        f.write(str(1 / c))
        f.write("\n")
        f.write(str(d))

except KeyboardInterrupt:
    time.sleep(0)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup()