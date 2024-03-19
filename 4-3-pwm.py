import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 1000)
p.start(0)

try:
    while True:
        t = input("Введите коэф. заполнения:")
        if t == "q":
            break
        a = int(t)
        p.ChangeDutyCycle(a)
        print("Напряжение:", 3.3 * a / 100, "В")

finally:
    p.stop()
    GPIO.cleanup()