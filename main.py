import json
import RPi.GPIO as GPIO
import time

#Assigning LED pins

led1Pin = 5
led2Pin = 6
led3Pin = 13

#Setting up the LED pins

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1Pin, GPIO.OUT)
GPIO.setup(led2Pin, GPIO.OUT)
GPIO.setup(led3Pin, GPIO.OUT)

#Setting up pwm to different pins

pwmLed1 = GPIO.PWM(led1Pin)
pwmLed2 = GPIO.PWM(led2Pin)
pwmLed3 = GPIO.PWM(led3Pin)

#Starting all of the LED's with them off

pwmLed1.start(0)
pwmLed2.start(0)
pwmLed3.start(0)

try:
  while True:
    with open('Lab4DataDup.txt','r') as f:
      data = json.load(f)
      ledSelected = data['LED']
      brightnessLevel = data['Brightness']
    if(ledSelected == '1'):
      pwmLed1.ChangeDutyCycle(brightnessLevel)
    elif(ledSelected == '2'):
      pwmLed2.ChangeDutyCycle(brightnessLevel)
    elif(ledSelected == '3'):
      pwmLed3.ChangeDutyCycle(brightnessLevel)
    time.sleep(.1)
          
except Exception as e:
  print('Error in the code')
  print(e)
