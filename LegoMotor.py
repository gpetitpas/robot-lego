from buildhat import Motor
import math
import atexit

class LegoMotor:
    def __init__(self, motor, default_speed=70) -> None:
        self.motor = Motor(motor)
        self.motor.set_default_speed(default_speed)
        self.reset_dist_counter()

        atexit.register(self.stop)
    
    def get_position(self):
        return self.motor.get_position() - self.dist_counter
    
    def get_wheel_position(self):
        return self.motor.get_aposition()
    
    def reset_dist_counter(self):
        self.dist_counter = self.motor.get_position()

    @staticmethod
    def convert_speed(speed):
        if (speed == 0):
            return 0
        elif (speed > 0):
            return math.floor(speed * 0.6) + 40
        else:
            return math.floor(speed * 0.6) - 40

    def start(self, speed=70):
        self.motor.start(self.convert_speed(speed))

    def stop(self):
        self.motor.stop()
