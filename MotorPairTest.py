from buildhat import MotorPair
import time
import math
from LegoMotorPair import LegoMotorPair

# https://buildhat.readthedocs.io/en/latest/buildhat/motor.html

# Next up:
# get diameter of the wheel, program to drive a certain distance forward/backward
# get width of robot, program to turn in place

# pair = MotorPair('A', 'B')
# pair.set_default_speed(70)

# pair.run_for_rotations(2)
# print('hi')
# pair.start(-70, 70)
# print('hi')
# time.sleep(2)
# pair.stop()
# print('end')

pair = LegoMotorPair('A', 'B', 70)
pair.start()
print('should convert to')
time.sleep(2)
pair.start(-20, 20)
print('hi 20')
time.sleep(2)
print('end')
