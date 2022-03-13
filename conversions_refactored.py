class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    value = float(value)
    if fromUnit == toUnit:
        return value
    elif fromUnit == "celsius" and toUnit == "kelvin":
        value = value + 273.15
        return round(value, 2)
    elif fromUnit == "celsius" and toUnit == "fahrenheit":
        value = value * (9 / 5) + 32
        return round(value, 2)
    elif fromUnit == "fahrenheit" and toUnit == "celsius":
        value = (value - 32) * (5 / 9)
        return round(value, 2)
    elif fromUnit == "fahrenheit" and toUnit == "kelvin":
        value = (value + 459.67) * (5 / 9)
        return round(value, 2)
    elif fromUnit == "kelvin" and toUnit == "fahrenheit":
        value = value * (9 / 5) - 459.67
        return round(value, 2)
    elif fromUnit == "kelvin" and toUnit == "celsius":
        value = value - 273.15
        return round(value, 2)
    elif fromUnit == "miles" and toUnit == "yards":
        value = value * 1760
        return round(value, 2)
    elif fromUnit == "miles" and toUnit == "meters":
        value = value * 1609.34
        return round(value, 2)
    elif fromUnit == "yards" and toUnit == "miles":
        value = value / 1760
        return round(value, 2)
    elif fromUnit == "yards" and toUnit == "meters":
        value = value * .9144
        return round(value, 2)
    elif fromUnit == "meters" and toUnit == "miles":
        value = value / 1609.34
        return round(value, 2)
    elif fromUnit == "meters" and toUnit == "yards":
        value = value / .9144
        return round(value, 2)
    else:
        raise ConversionNotPossible(f'Incompatible units. Unable to convert from {fromUnit} to {toUnit}.')