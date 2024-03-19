import RPi.GPIO as GPIO

def dec2bin(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        t = input("Введите целое число от о до 255:")
        if t == "q":
            break
        a = int(t)
        if a < 0:
            print("Введённое число отрицательно")
            break
        if a > 255:
            print("Введённое число превышает 8 разрядов")
            break
        GPIO.output(dac, dec2bin(a))
        print("Напряжение:", a/(256) * 3.3, "В")

except ValueError:
    try:
        t = float(t)
        print("Введённое число не является целым")
    except ValueError:
        print("Введено не число")

finally:
    GPIO.output(dac, 0) 
    GPIO.cleanup()