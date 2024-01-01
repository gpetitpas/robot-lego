from buildhat import MotorPair
import time
import math
from Robot import Robot

# https://buildhat.readthedocs.io/en/latest/buildhat/motor.html

# Next up:
# get diameter of the wheel, program to drive a certain distance forward/backward
# get width of robot, program to turn in place


def basic_obstacle_avoidance(robot):    
    while True:
        dist = robot.dist_sensor.get_distance()
        print("dist: {d}".format(d=dist))
        if dist < 70:
            print("reverse")
            robot.stop()
            time.sleep(1)
            robot.start(70, -70) # reverse
            time.sleep(1.5)
            robot.stop()
            robot.spin_clockwise()
            robot.stop()
            time.sleep(1)
        else:
            print("forward")
            robot.start()
        time.sleep(0.1)

def beginner_driving(robot):
    robot.drive_straight(2)
    robot.turn_right()
    robot.turn_left()
    robot.drive_straight(1)
    robot.spin_clockwise()


def main():
    robot = Robot()
    basic_obstacle_avoidance(robot=robot)


if __name__ == "__main__":
    main()