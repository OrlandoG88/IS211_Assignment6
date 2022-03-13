def convertCelsiusToKelvin(celsius):
	kelvin = 273.15 + celsius

	return round(kelvin, 2)


def convertCelsiusToFahrenheit(celsius):
	fahrenheit = 1.8 * celsius + 32

	return round(fahrenheit, 2)

def convertFahrenheitToCelsius(fahrenheit):

	celsius = ((fahrenheit - 32) * (5/9))

	return round(celsius, 2)

def convertFahrenheitToKelvin(fahrenheit):

	kelvin = ((fahrenheit - 32) * (5/9) + 273.15)

	return round(kelvin, 2)


def convertKelvinToCelsius(kelvin):
	celsius = kelvin - 273.15

	return round(celsius, 2)



def convertKelvinToFahrenheit(kelvin):

	fahrenheit = kelvin * 9/5 - 459.67

	return round(fahrenheit, 2)




