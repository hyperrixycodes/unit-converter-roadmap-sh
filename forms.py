from django import forms

class LengthForm(forms.Form):
    value = forms.FloatField(label="Value")
    from_unit = forms.ChoiceField(choices=[
        ('millimiter', 'Millimiter'),
        ('centimeter', 'Centimeter'),
        ('meter', 'Meter'),
        ('kilometer', 'Kilometer'),
        ('inch', 'Inch'),
        ('foot', 'Foot'),
        ('yard', 'Yard'),
        ('mile', 'Mile'),
    ])
    to_unit = forms.ChoiceField(choices=[
        ('millimiter', 'Millimiter'),
        ('centimeter', 'Centimeter'),
        ('meter', 'Meter'),
        ('kilometer', 'Kilometer'),
        ('inch', 'Inch'),
        ('foot', 'Foot'),
        ('yard', 'Yard'),
        ('mile', 'Mile'),
    ])

class WeightForm(forms.Form):
    value = forms.FloatField(label="Value")
    from_unit = forms.ChoiceField(choices=[
        ('milligram', 'Milligram'),
        ('gram', 'Gram'),
        ('kilogram', 'Kilogram'),
        ('ounce', 'Ounce'),
        ('pound', 'Pound'),
    ])

    to_unit = forms.ChoiceField(choices=[
        ('milligram', 'Milligram'),
        ('gram', 'Gram'),
        ('kilogram', 'Kilogram'),
        ('ounce', 'Ounce'),
        ('pound', 'Pound'),
    ])

class TemperatureForm(forms.Form):
    value = forms.FloatField(label="Value")
    from_unit = forms.ChoiceField(choices=[
        ('celcius', 'Celcius'),
        ('kelvin', 'Kelvin'),
        ('farenheit', 'Farenheit'),
    ])
    to_unit = forms.ChoiceField(choices=[
        ('celcius', 'Celcius'),
        ('kelvin', 'Kelvin'),
        ('farenheit', 'Farenheit'),
    ])