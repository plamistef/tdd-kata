import unittest
from converter import Converter

class test(unittest.TestCase):

    def test_calculate(self):
        c = Converter()
        self.assertEqual(c.calculate("MCMXLIV"),1944)
        self.assertEqual(c.calculate("MMMDCCXXIV"),3724)
        self.assertEqual(c.calculate("MMCXXIV"),2124)

    def test_validate(self):
        c = Converter()
        self.assertTrue(c.validate("MCMXLIV"))
        self.assertFalse(c.validate("AXLIV"))
        self.assertFalse(c.validate("123"))
    
    def test_covert(self):
        c = Converter()
        self.assertEqual(c.convert("ABVC"),"Invalid number")
        self.assertEqual(c.convert("CMXLIV"),944)
        self.assertEqual(c.convert("DCCLXXXIX"),789)

if __name__ == '__main__':
    unittest.main()