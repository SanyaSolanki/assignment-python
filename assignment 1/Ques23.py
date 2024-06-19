#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


while True:
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.\n")
        
    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.\n")
        

    
    else:
        print("Invalid choice. Please enter 1, 2.\n")
        break
