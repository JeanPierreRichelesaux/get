import RPi.GPIO as rp
import time

rp.setmode(rp.BCM)

rp.setup(21, rp.OUT)

for _ in range(5):
    rp.output(21, 1)
    time.sleep(1)
    rp.output(21, 0)
    time.sleep(1)



