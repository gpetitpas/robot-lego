import time

from LegoMotorPair import LegoMotorPair

class Robot:
    def __init__(self) -> None:
        self.pair = LegoMotorPair('A', 'B', 70)


    def drive_straight(self, seconds):
        self.pair.start()
        time.sleep(seconds)

    def turn_left(self):
        self.pair.start(50, 50)
        time.sleep(0.45)

    def turn_right(self):
        self.pair.start(-50, -50)
        time.sleep(0.45)

    def spin_clockwise(self):
        self.pair.start(-50, -50)
        time.sleep(1.8)