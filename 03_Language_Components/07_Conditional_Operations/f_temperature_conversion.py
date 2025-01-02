#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""

# Program for temperature conversions

# Input from the user
user_input = input("Enter the temperature (e.g., 23C or 23F): ").strip()

# Check for valid input
if len(user_input) < 2:
    print("Invalid input. Please provide a valid temperature (e.g., 23C or 23F).")
else:
    # Extract the numeric part and the unit
    temp_value = user_input[:-1].strip()  # Everything except the last character
    unit = user_input[-1].strip().upper()  # Last character (case-insensitive)

    # Validate the numeric part
    if not temp_value.replace('.', '', 1).isdigit():  # Allow decimal numbers
        print("Invalid temperature value. Please enter a valid number.")
    else:
        temp_value = float(temp_value)  # Convert the numeric part to a float

        # Check the unit and perform the conversion
        if unit == "C":
            # Celsius to Fahrenheit
            fahrenheit = (temp_value * 9/5) + 32
            print(f"{temp_value}C is equivalent to {fahrenheit:.2f}F.")
        elif unit == "F":
            # Fahrenheit to Celsius
            celsius = (temp_value - 32) * 5/9
            print(f"{temp_value}F is equivalent to {celsius:.2f}C.")
        else:
            print("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")
