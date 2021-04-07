import unittest
from DecimalConverter import DecimalConverter
from RomanConverter import RomanConverter

class test(unittest.TestCase):

    def test_rom_calculate(self):
        c = RomanConverter()
        self.assertEqual(c.calculate("MCMXLIV"),1944)
        self.assertEqual(c.calculate("MMMDCCXXIV"),3724)
        self.assertEqual(c.calculate("MMCXXIV"),2124)

    def test_rom_validate(self):
        c = RomanConverter()
        self.assertTrue(c.validate("MCMXLIV"))
        self.assertFalse(c.validate("AXLIV"))
        self.assertFalse(c.validate("123"))
    
    def test_rom_convert(self):
        c = RomanConverter()
        self.assertEqual(c.convert("ABVC"),"Invalid number")
        self.assertEqual(c.convert("CMXLIV"),944)
        self.assertEqual(c.convert("DCCLXXXIX"),789)

    def test_dec_calculate(self):
        dc = DecimalConverter()
        self.assertEqual(dc.calculate(2330),"MMCCCXXX")
        self.assertEqual(dc.calculate(1245),"MCCXLV")
        self.assertEqual(dc.calculate(3490),"MMMCDXC")
    
    def test_dec_convert(self):
        dc = DecimalConverter()
        self.assertEqual(dc.convert(3.5),"Invalid number")
        self.assertEqual(dc.convert(456),"CDLVI")
        self.assertEqual(dc.convert(245),"CCXLV")

if __name__ == '__main__':
    unittest.main()