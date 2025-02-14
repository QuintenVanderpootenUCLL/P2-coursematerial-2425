class Duration:
    def __init__(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
    
    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours
    
    @staticmethod
    def from_seconds(number):
        return Duration(number, number/60, number/3600)
    

    @staticmethod
    def from_minutes(number):
        return Duration(number * 60, number , number / 60)
    
    @staticmethod
    def from_hours(number):
        return Duration(number * 3600, number * 60 ,  number)