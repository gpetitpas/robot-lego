from buildhat import MotorPair
import time
import math
from Robot import Robot

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

robot = Robot()

robot.drive_straight(2)
robot.turn_right()
robot.turn_left()
robot.drive_straight(1)
robot.spin_clockwise()

