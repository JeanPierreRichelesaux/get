import RPi.GPIO as GPIO
#import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
num = [0,0,0,0,0,0,0,0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, num)
#time.sleep(12)

GPIO.output(dac, 0) 
GPIO.cleanup()

x = [2, 174, 255, 127, 64, 32, 5, 0]
y = [0.0796,2.268,3.237,1.673,0.868,0.46,0.1183,0.054]
plt.scatter(x,y)
plt.plot(x,y)
plt.ylabel('U, V')
plt.xlabel('N')
plt.show()