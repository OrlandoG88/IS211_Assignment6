import unittest
from conversion import *
from conversions_refactored import convert, ConversionNotPossible


class Refactored_Conversions_Test(unittest.TestCase):


    def test_convert(self):
        self.assertEqual(convert('celsius', 'kelvin', 80.0), 353.15)


    def test_convert(self):
        self.assertEqual(convert('celsius', 'fahrenheit', 80.0), 176.0)


    def test_convert(self):
        self.assertEqual(convert('fahrenheit', 'celsius', 80.0), 26.67)


    def test_convert(self):
        self.assertEqual(convert('fahrenheit', 'kelvin', 80.0), 29.82)


    def test_convert(self):
        self.assertEqual(convert('kelvin', 'fahrenheit', 80.0), -315.67)


    def test_convert(self):
        self.assertEqual(convert('kelvin', 'celsius', 80.0), -193.15)


    def test_convert(self):
        self.assertEqual(convert('miles', 'yards', 32.50),  57200)


    def test_convert(self):
        self.assertEqual(convert('miles', 'meters', 16.25), 26151.77)


    def test_convert(self):
        self.assertEqual(convert('yards', 'miles', 250.00), .14)


    def test_convert(self):
        self.assertEqual(convert('yards', 'meters', 2917.00), 2667.30)


    def test_convert(self):
        self.assertEqual(convert('meters', 'miles', 16517.50), 10.26)


    def test_convert(self):
        self.assertEqual(convert('meters', 'yards', 6500.00), 7108.49)

    def test_convertSameFromToUnits(self):
        self.assertEqual(convert('meters', 'meters', 1800.95), 1800.95)

    def test_convertIncompatibleUnits(self):
        self.assertRaises(ConversionNotPossible, convert, 'celsius', 'meters', 300)




class conversion_testing(unittest.TestCase):



    def test_convertFahrenheitToCelsius(self):
        '''convertFahrenheitToCelsius should give known result with known input'''
        self.assertEqual(convertFahrenheitToCelsius(80), 26.67, msg="80 F = 26.66 C")
        self.assertEqual(convertFahrenheitToCelsius(200), 93.33, msg="200 F = 93.33 C")
        self.assertEqual(convertFahrenheitToCelsius(40), 4.44, msg="40 F = 4.44 C")
        self.assertEqual(convertFahrenheitToCelsius(-20), -28.89, msg="-20 F = -28.89 C")
        self.assertEqual(convertFahrenheitToCelsius(32), 0,msg= "32 F = 0 C")

    def test_convertKelvinToCelsius(self):
        '''convertKelvinToCelsius should give known result with known input'''
        self.assertEqual(convertKelvinToCelsius(80), -193.15, msg="80 K = -193.15 C")
        self.assertEqual(convertKelvinToCelsius(200), -73.15, msg="200 K = -73.15 C")
        self.assertEqual(convertKelvinToCelsius(40), -233.15,msg= "40 K = -233.15 C")
        self.assertEqual(convertKelvinToCelsius(-20), -293.15, msg="-20 K = -293.15 C")
        self.assertEqual(convertKelvinToCelsius(32), -241.15, msg="32 K = -241.15 C")

    def test_convertCelsiusToFahrenheit(self):
        '''convertCelsiusToFahrenheit should give known result with known input'''
        self.assertEqual(convertCelsiusToFahrenheit(80), 176, msg="80 C = 176 F")
        self.assertEqual(convertCelsiusToFahrenheit(200), 392,msg= "200 C = 392 F")
        self.assertEqual(convertCelsiusToFahrenheit(40), 104, msg="40 C = 104 F")
        self.assertEqual(convertCelsiusToFahrenheit(-20), -4, msg="-20 C = -4 F")
        self.assertEqual(convertCelsiusToFahrenheit(32), 89.6, msg="32 C = 89.6 F")


    def test_convertKelvinToFahrenheit(self):
        '''convertKelvinToFahrenheit should give known result with known input'''
        self.assertEqual(convertKelvinToFahrenheit(80), -315.67, msg="80 K = -315.67 F")
        self.assertEqual(convertKelvinToFahrenheit(200), -99.67,msg= "200 K = -99.67 F")
        self.assertEqual(convertKelvinToFahrenheit(40), -387.67, msg="40 K = -387.67 F")
        self.assertEqual(convertKelvinToFahrenheit(-20), -495.67, msg="-20 K = -495.67 F")
        self.assertEqual(convertKelvinToFahrenheit(32), -402.07, msg="32 K = -402.07 F")

    def test_convertCelsiusToKelvin(self):
        '''convertCelsiusToKelvin should give known result with known input'''
        self.assertEqual(convertCelsiusToKelvin(80), 353.15, msg="80 C = 353.15 K")
        self.assertEqual(convertCelsiusToKelvin(200), 473.15, msg="200 C = 473.15 K")
        self.assertEqual(convertCelsiusToKelvin(40), 313.15, msg="40 C = 313.15 K")
        self.assertEqual(convertCelsiusToKelvin(-20), 253.15, msg="-20 C = 253.15 K")
        self.assertEqual(convertCelsiusToKelvin(32), 305.15, msg="32 C = 305.15 K")

    def test_convertFahrenheitToKelvin(self):
        '''convertFahrenheitToKelvin should give known result with known input'''
        self.assertEqual(convertFahrenheitToKelvin(80), 299.82, msg ="80 F = 299.81 K")
        self.assertEqual(convertFahrenheitToKelvin(200), 366.48, msg ="200 F = 366.48 K")
        self.assertEqual(convertFahrenheitToKelvin(40), 277.59, msg= "40 F = 277.59 K")
        self.assertEqual(convertFahrenheitToKelvin(-20), 244.26, msg= "-20 F =  244.26 K")
        self.assertEqual(convertFahrenheitToKelvin(32), 273.15, msg="32 F = 273.15 K")





if __name__ == '__main__':
    unittest.main()
