from __future__ import division
from flask import Flask,request,render_template
import time as t
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import time as t
import Adafruit_CharLCD as LCD

lcd_rs = 12
lcd_en = 13
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 26
lcd_d7 = 22
lcd_backlight = 2

lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows,lcd_backlight)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led1=19
led2=16
led3=20
led4=5
GPIO.setup(led1, GPIO.OUT)
GPIO.output(led1, 0)
GPIO.setup(led2, GPIO.OUT)
GPIO.output(led2, 0)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led3, 0)
GPIO.setup(led4, GPIO.OUT)
GPIO.output(led4, 0)



app = Flask(__name__)
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
lcd.clear()
lcd.message("L1:OFF    L2:OFF\nL3:OFF    L4:OFF")

@app.route('/')
def index():
	
	return render_template('index.html')

@app.route('/otvori')
def otvaranje():
	pwm.set_pwm(15,0,356)
	print("otvoreno")
	return render_template("index.html")

@app.route('/zatvori')
def zatvaranje():
	pwm.set_pwm(15,0,630)
	print("zatvoreno")
	return render_template("index.html")

@app.route('/otvorig')
def otvaranjeg():
	pwm.set_pwm(14,0,356)
	print("otvoreno")
	return render_template("index.html")

@app.route('/zatvorig')
def zatvaranjeg():
	pwm.set_pwm(14,0,630)
	print("zatvoreno")
	return render_template("index.html")

@app.route('/led1on')
def led1u():
		GPIO.output(led1,GPIO.HIGH)
		lcd.set_cursor(0,0)
		lcd.message('L1:ON     ')
		return index()

@app.route('/led1off')
def led1ug():
		GPIO.output(led1,GPIO.LOW)
		lcd.set_cursor(0,0)
		lcd.message('L1:OFF    ')
		return index()

@app.route('/led2on')
def led2u():
		GPIO.output(led2,GPIO.HIGH)
		lcd.set_cursor(10,0)
		lcd.message('L2:ON \n')
		return index()

@app.route('/led2off')
def led2ug():
		GPIO.output(led2,GPIO.LOW)
		lcd.set_cursor(10,0)
		lcd.message('L2:OFF\n')
		return index()

@app.route('/led3on')
def led3u():
		GPIO.output(led3,GPIO.HIGH)
		lcd.set_cursor(0,1)
		lcd.message('L3:ON     ')
		return index()

@app.route('/led3off')
def led3ug():
		GPIO.output(led3,GPIO.LOW)
		lcd.set_cursor(0,1)
		lcd.message('L3:OFF')
		return index()

@app.route('/led4on')
def led4u():
		GPIO.output(led4,GPIO.HIGH)
		lcd.set_cursor(10,1)
		lcd.message('L4:ON ')

		return index()

@app.route('/led4off')
def led4ug():
		GPIO.output(led4,GPIO.LOW)
		lcd.set_cursor(10,1)
		lcd.message('L4:OFF')

		return index()
	


if __name__=='__main__':
          app.run( host='0.0.0.0' , port=1000 , debug=True, threaded=True)
