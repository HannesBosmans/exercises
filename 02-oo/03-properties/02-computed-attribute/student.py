# Write your code here
class BMICalculator:
    def __init__(self,weight_in_kg,height_in_m):
        self.__weight_in_kg = weight_in_kg
        self.__heigth_in_m = height_in_m

    @property
    def weigth_in_kg(self):
        return self.__weight_in_kg
    @property
    def heigth_in_m(self):
        return self.__heigth_in_m
    @property
    def bmi(self):
        return self.weigth_in_kg / self.heigth_in_m **2
    @property
    def category(self):
        if self.bmi < 18.5:
            return "underweigth"
        elif 18.5< self.bmi < 25:
            return "normal"
        else: return "overweight"

calc = BMICalculator(80,1.80)
print(calc.bmi)
print(calc.category)
