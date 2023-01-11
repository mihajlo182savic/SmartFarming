from __future__ import division
import time as t
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

try:
	while(True):
		pwm.set_pwm(15,0,630)
		print("zatvoreno")		
		t.sleep(5)
		
		pwm.set_pwm(15,0,356)
		print("otvoreno")
		t.sleep(5)

except(KeyboardInterrupt):
	pwm.set_pwm(15,0,0)
