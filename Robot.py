import math
import time

from LegoDistanceSensor import LegoDistanceSensor
from LegoMotorPair import LegoMotorPair
from LegoMotor import LegoMotor


wheel_diameter          = 57 # in millimeters (mm)
ticks_per_revolution    = 360
ticks_to_mm = (math.pi / ticks_per_revolution) * wheel_diameter


class Robot:
    def __init__(self) -> None:
        # self.pair = LegoMotorPair('A', 'B', 70)
        self.dist_sensor = LegoDistanceSensor('D')
        self.left_motor = LegoMotor('A')
        self.right_motor = LegoMotor('B')


    def start(self, left_speed=-70, right_speed=70):
        self.left_motor.start(left_speed)
        self.right_motor.start(right_speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    # For encoder ticks, use the output from motor.get_position()
    def ticks_to_mm(self, encoder_ticks):
        return int(ticks_to_mm * encoder_ticks)
    
    def drive_distance(self, distance):
        ticks = distance / ticks_to_mm
        print("driving for: {} distance, {} ticks".format(distance, ticks))
        
        # Get start from left motor and right motor
        # left is moving backward fyi
        l_start_pos = self.left_motor.get_position()
        l_target_pos = l_start_pos - ticks
        print("target: {}".format(l_target_pos))

        # start motors
        self.left_motor.start(-70)

        # stop when left pos = start left + dist, when right
        while self.left_motor.get_position() > l_target_pos:
            print(self.left_motor.get_position())
            time.sleep(0.05)
        self.left_motor.stop()


    # def drive_straight(self, seconds):
    #     self.pair.start()
    #     time.sleep(seconds)
    #     self.pair.stop()
    #     time.sleep(0.1)

    # def turn_left(self):
    #     self.pair.start(50, 50)
    #     time.sleep(0.45)
    #     self.pair.stop()
    #     time.sleep(0.1)

    # def turn_right(self):
    #     self.pair.start(-50, -50)
    #     time.sleep(0.45)
    #     self.pair.stop()
    #     time.sleep(0.1)

    # def spin_clockwise(self):
    #     self.pair.start(-50, -50)
    #     time.sleep(1.8)
    #     self.pair.stop()
    #     time.sleep(0.1)