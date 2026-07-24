# This Converts temperatures between Celsius, Fahrenheit, and Kelvin.

# Get input from the user

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (K, C, or F): ").upper()

# Check if the unit is valid

if unit == "K" or unit == "C" or unit == "F":

    print("\nTemperature Conversions:")
    print(f"{temperature:.4f} °{unit}" if unit != "K" else f"{temperature:.4f} K")

    if unit == "C":

        # Convert Celsius to Fahrenheit and Kelvin

        fahrenheit = (temperature * 9 / 5) + 32
        kelvin = temperature + 273.15

        print(f"{fahrenheit:.4f} °F")
        print(f"{kelvin:.4f} K")

    elif unit == "F":

        # Convert Fahrenheit to Celsius and Kelvin

        celsius = (temperature - 32) * 5 / 9
        kelvin = (temperature - 32) * 5 / 9 + 273.15

        print(f"{celsius:.4f} °C")
        print(f"{kelvin:.4f} K")

    else:
        # Convert Kelvin to Celsius and Fahrenheit

        celsius = temperature - 273.15
        fahrenheit = (temperature - 273.15) * 9 / 5 + 32

        print(f"{celsius:.4f} °C")
        print(f"{fahrenheit:.4f} °F")

else:
    print("Invalid unit. Please use K, C, or F.")