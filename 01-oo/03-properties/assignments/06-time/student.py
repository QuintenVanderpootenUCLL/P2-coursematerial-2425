# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self, number):
        if 0 <= number <= 23:
            self.__hours = number
        else:
            raise(ValueError())
    
    @minutes.setter
    def minutes(self, number):
        if 0 <= number <= 59:
                self.__minutes = number
        else:
            raise(ValueError())
        
    @seconds.setter
    def seconds(self, number):
        if 0 <= number <= 59:
            self.__seconds = number
        else:
            raise(ValueError())