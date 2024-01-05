from buildhat import MotorPair
import math
import atexit

class LegoMotorPair:
    def __init__(self, left_motor, right_motor, default_speed=70) -> None:
        self.pair = MotorPair(left_motor, right_motor)
        self.default_speed = default_speed
        self.pair.set_default_speed(default_speed)

        atexit.register(self.stop)

    @staticmethod
    def convert_speed(speed):
        if (speed == 0):
            return 0
        elif (speed > 0):
            # print("Speed is: {}".format(math.floor(speed * 0.6) + 40))
            return math.floor(speed * 0.6) + 40
        else:
            # print("Speed is: {}".format(math.floor(speed * 0.6) - 40))
            return math.floor(speed * 0.6) - 40

    def start(self, left_speed=-70, right_speed=70):
        self.pair.start(self.convert_speed(left_speed), self.convert_speed(right_speed))

    def stop(self):
        self.pair.stop()