# Write your code here
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.bmi = weight_in_kg / height_in_m **2
        

    @property
    def category(self):
        if self.bmi > 18.5 and self.bmi < 25:
            return "normal"
        elif self.bmi < 18.5:
            return "underweight"
        
        else:
            return "overweight"

calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)
print(calc.bmi)
print(calc.category)