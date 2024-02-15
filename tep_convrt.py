# Create a program that allows the user to convert temperatures between Fahrenheit and
# Celsius..
def temp_convert():
    temperature = float(input("Enter the temperature :"))
    unit = input("Enter the unit(F for fahrenhiet) (C for Celsius) :")
    
    if unit.upper() == 'F':
        celsius = (temperature - 32) * 5/9
        print(f"{temperature} degree is equal to {celsius} degree Celsius:")
    elif unit.upper() == 'C':
        fahrenhiet = (temperature * 9/5) + 32
        print(f"{temperature} degree is equal to {fahrenhiet} degree Farenhiet:")
    else:
        print("Invalid unit.Please Enter F or C")

temp_convert()


