import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
crvena=19
GPIO.setup(crvena, GPIO.OUT)
try:
    while  (True):
		GPIO.output(crvena,GPIO.HIGH)
		t.sleep(1)
		GPIO.output(crvena,GPIO.LOW)
		t.sleep(1)
	
except KeyboardInterrupt:
    GPIO.cleanup()
