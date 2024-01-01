from buildhat import DistanceSensor

class LegoDistanceSensor:
    def __init__(self, distance_sensor_port, threshold_distance=100) -> None:
        self.dist_sensor = DistanceSensor(distance_sensor_port, threshold_distance)

    def get_distance(self):
        return self.dist_sensor.get_distance()
