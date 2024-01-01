from buildhat import MotorPair
import time
import math
from Robot import Robot

# https://buildhat.readthedocs.io/en/latest/buildhat/motor.html

# Next up:
# get diameter of the wheel, program to drive a certain distance forward/backward
# get width of robot, program to turn in place

robot = Robot()

while True:
    print(robot.dist_sensor.get_distance())
    time.sleep(0.1)

# robot.drive_straight(2)
# robot.turn_right()
# robot.turn_left()
# robot.drive_straight(1)
# robot.spin_clockwise()

