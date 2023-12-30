from buildhat import MotorPair
import time
import math

# https://buildhat.readthedocs.io/en/latest/buildhat/motor.html

# Next up:
# get diameter of the wheel, program to drive a certain distance forward/backward
# get width of robot, program to turn in place

pair = MotorPair('A', 'B')
pair.set_default_speed(70)

pair.run_for_rotations(2)
print('hi')