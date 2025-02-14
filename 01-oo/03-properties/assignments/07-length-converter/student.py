class LengthConverter:
    def __init__(self):
        self.distance_in_meter = 0
    @property
    def distance_in_meter(self):
        return self.__distance_in_meter
    
    @distance_in_meter.setter
    def meter(self, number, unit):
        if unit == "meter":
            self.__distance_in_meter = number
        elif unit == "inch":
            self.__distance_in_meter = number * 39.3701
        
        elif unit == "feet":
            self.__distance_in_meter = number * 3.2808
    

    

