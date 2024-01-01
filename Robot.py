import time

from LegoDistanceSensor import LegoDistanceSensor
from LegoMotorPair import LegoMotorPair

class Robot:
    def __init__(self) -> None:
        self.pair = LegoMotorPair('A', 'B', 70)
        self.dist_sensor = LegoDistanceSensor('D')


    def start(self):
        self.pair.start()

    def stop(self):
        self.pair.stop()

    def drive_straight(self, seconds):
        self.pair.start()
        time.sleep(seconds)
        self.pair.stop()
        time.sleep(0.1)

    def turn_left(self):
        self.pair.start(50, 50)
        time.sleep(0.45)
        self.pair.stop()
        time.sleep(0.1)

    def turn_right(self):
        self.pair.start(-50, -50)
        time.sleep(0.45)
        self.pair.stop()
        time.sleep(0.1)

    def spin_clockwise(self):
        self.pair.start(-50, -50)
        time.sleep(1.8)
        self.pair.stop()
        time.sleep(0.1)