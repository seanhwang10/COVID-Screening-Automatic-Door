import RPi.GPIO as GPIO   # We need this library to access GPIO pins
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 16  # These are the GPIO pin numbers that we will use
Motor1B = 18
Motor1E = 22

LimitSwitchUp = 12 # The limit switch is connected to this pin

GPIO.setup(Motor1A, GPIO.OUT)       # OUT means we will output to this pin
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(LimitSwitchUp, GPIO.IN)  # IN means we will listen to this pin

print "Turning motor on"

GPIO.output(Motor1A, GPIO.LOW)      # Send low voltage to 1A
GPIO.output(Motor1B, GPIO.HIGH)     # Send high voltage to 1B
GPIO.output(Motor1E, GPIO.HIGH)     # Activate the motor

maxDur = 150
curDur = 0
pollInterval = 0.001
roomToGo = GPIO.input(LimitSwitchUp)

# We are now listening the status of the limit switch for
# 150 seconds, checking it every 0.001 seconds.
while roomToGo == 1 and curDur <= maxDur:
    sleep(pollInterval)
    curDur = curDur + pollInterval
    roomToGo = GPIO.input(LimitSwitchUp)

# Roll back down a little to release the switch
while GPIO.input(LimitSwitchUp) == 0:
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    sleep(pollInterval)

print "Stopping motor"

GPIO.output(Motor1E, GPIO.LOW) # Deactivate the motor
GPIO.cleanup()

