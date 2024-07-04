import board
import digitalio
import pulseio
import time
from adafruit_motor import servo
servopower = digitalio.DigitalInOut(board.D22)
servopower.direction = digitalio.Direction.OUTPUT
#Gpio pin 22 is set to output
pwm5 = pulseio.PWMOut(board.D5, frequency=50)
pwm23 = pulseio.PWMOut(board.D23, frequency=50)
pwm6 = pulseio.PWMOut(board.D6, frequency=50)
kitsune_arm1 = servo.Servo(pwm5)
kitsune_arm2 = servo.Servo(pwm23)
kitsune_head = servo.Servo(pwm6)
kitsune_arm1.angle = 90
time.sleep(2)
kitsune_arm2.angle = 90
time.sleep(2)
kitsune_head.angle = 90



    


