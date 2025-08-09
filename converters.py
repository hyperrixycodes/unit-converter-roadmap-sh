length_list = {
    'millimiter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34,
}

def convert_length(value, from_unit, to_unit):
    meters = value * length_list[from_unit]
    return meters / length_list[to_unit]

weight_list = {
    'milligram': 0.00001,
    'gram': 0.001,
    'kilogram': 1,
    'pound': 0.4536,
    'ounce': 0.0283,
}

def convert_weight(value, from_unit, to_unit):
    kilograms = value * weight_list[from_unit]
    return kilograms / weight_list[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'kelvin':
        celcius = value - 273.15
    elif from_unit == 'celcius':
        celcius = value
    elif from_unit == 'farenheit':
        celcius = (value - 32) * 5/9

    if to_unit == 'kelvin':
        return celcius + 273.15
    elif to_unit == 'farenheit':
        return (celcius * 9/5) + 32 
    else:
        return celcius

