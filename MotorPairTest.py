import time
import math
import logging

from Robot import Robot

# https://buildhat.readthedocs.io/en/latest/buildhat/motor.html

# Next up:
# get diameter of the wheel, program to drive a certain distance forward/backward
# get width of robot, program to turn in place


def basic_obstacle_avoidance(robot):    
    while True:
        dist = robot.dist_sensor.get_distance()
        print("dist: {d}".format(d=dist))
        if dist == -1:
            print("pausing")
            continue
        elif dist < 70:
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

def configure_logging():
    logger = logging.getLogger("robot logs")
    logging.basicConfig(level=logging.INFO)
    return logger

def check_encoders(robot, logger):
    stop_time = time.time() + 1
    robot.start()
    while time.time() < stop_time:
        logger.info("Left: {}, Right: {}".format(
            robot.ticks_to_mm(robot.left_motor.get_position()), 
            robot.ticks_to_mm(robot.right_motor.get_position())))
        time.sleep(0.05)
    robot.stop()
  

def main():
    logger = configure_logging()
    logger.info("Log is working!")
    # logger has to come first, apparently
    robot = Robot()

    robot.drive_distance(180)
    #check_encoders(robot, logger)
    # basic_obstacle_avoidance(robot=robot)


if __name__ == "__main__":
    main()