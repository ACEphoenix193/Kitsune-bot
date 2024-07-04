import board
import digitalio
import pulseio
import time
from adafruit_motor import servo
servopower = digitalio.DigitalInOut(board.D22)
pin23 = digitalio.DigitalInOut(board.D23)
#Access gpio pin 22 and 23

servopower.direction = digitalio.Direction.OUTPUT
#Gpio pin 22 is set to output
pwm23 = pulseio.PWMOut(board.D23, frequency=50)
my_servo = servo.Servo(pwm23)
my_servo.angle = 90


    


