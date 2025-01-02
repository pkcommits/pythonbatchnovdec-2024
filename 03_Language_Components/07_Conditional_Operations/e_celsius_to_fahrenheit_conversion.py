"""
Purpose: Temperature Conversions
    - celsius to fahrenheit
"""

temp = float(input("Enter temperature in Celsius: "))

if temp:
    fahrenheit = (temp * 9 / 5) + 32
    print(f'The temperature in F is {fahrenheit}')
else:
    print('Error in conversion! Try again')