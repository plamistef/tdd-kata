import re
class Converter():

    def __init__(self):
        self.numbers = {"I":1,"V":5, "X":10, "L":50,"C":100, "D":500, "M":1000}

    def convert(self,roman_num):
        result = 0
        if (self.validate(roman_num)):
            result = self.calculate(roman_num)
        else:
            result = "Invalid number"
        return result

    def calculate(self,rom):
        prev = 0 
        ans = 0
        n = len(rom)
        for i in range(n-1, -1, -1):
    
            # If greater than or equal to previous,
            # add to answer
            if self.numbers[rom[i]] >= prev:
                ans += self.numbers[rom[i]]
    
            # If smaller than previous
            else:
                ans -= self.numbers[rom[i]]
    
            # Update previous
            prev = self.numbers[rom[i]]
        return ans   

    def validate(self,string):
        return(bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string)))