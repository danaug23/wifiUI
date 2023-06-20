import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 50)

pwm.start(0)

pwm.ChangeDutyCycle(5)
sleep(.225)
pwm.ChangeDutyCycle(10)
sleep(.2)
print("done")
pwm.stop()
GPIO.cleanup()
print("cleanup")
