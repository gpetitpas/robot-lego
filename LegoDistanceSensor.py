from buildhat import DistanceSensor
import time

class LegoDistanceSensor:
    def __init__(self, distance_sensor_port, threshold_distance=100) -> None:
        self.dist_sensor = DistanceSensor(distance_sensor_port, threshold_distance)

    def get_distance(self):
        vals = []
        for val in range(3):
            vals.append(self.dist_sensor.get_distance())
            time.sleep(0.05)
        
        sum = 0
        count = 0
        for val in range(3):
            if (vals[val] != -1):
                count += 1
                sum += vals[val]
        if (count > 0):
            return sum / count
        else:
            return -1
