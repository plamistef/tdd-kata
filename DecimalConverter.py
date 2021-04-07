class DecimalConverter():
    def __init__(self):
        self.roman_letters = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                  (90, 'XC'),  (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                  (5, 'V'), (4, 'IV'), (1, 'I')]
    
    def convert(self,decimal_num):
        result = 0
        if (isinstance(decimal_num, int)):
            result = self.calculate(decimal_num)
        else:
            result = "Invalid number"
        return result
    
    def calculate(self, num):
        output = []
        for value, letter in self.roman_letters:
            n = num // value               
            output.extend([letter] * n)    
            num -= n * value               
        return "".join(output)
