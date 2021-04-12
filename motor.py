import RPi.GPIO as GPIO
#importing file line 
from time import sleep

doordet = 1

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

LimitSwitchDown = 11
LimitSwitchUp = 12

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(LimitSwitchDown, GPIO.IN) # Note that we are listening to both limit switches
GPIO.setup(LimitSwitchUp, GPIO.IN)

print ("Turning motor on")

GPIO.output(Motor1A, GPIO.HIGH) # Note that the polarity is reversed with respect to "openLimit.py"
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH) # Activate the motor

maxDur = 150
curDur = 0
pollInterval = 0.001

# Again loop for a maximum of 150 seconds by checking the status the switches
while curDur <= maxDur:
    if doordet == 0:
        roomToGoDown = GPIO.input(LimitSwitchDown)
    if doordet == 1:
        roomToGoUp = GPIO.input(LimitSwitchUp)

    if roomToGoUp == 0: # The top is wound back on the reel, so we must reverse
        # Reverse direction
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        sleep(1) # allow time for the switch to be released
        curDur = 0; # reset timer to give another 150 seconds

    if roomToGoDown == 0: # The door is closed
        break

    sleep(pollInterval)
    curDur = curDur + pollInterval

print ("Stopping motor")

GPIO.output(Motor1E, GPIO.LOW) # Deactivate the motor
GPIO.cleanup()
