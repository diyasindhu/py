# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
choice = int(input("Enter 1 to convert temperature from Celsius to Farenheit\n\
Enter 2 to convert temperature from Farenheit to Celsius:\n "))
if(choice==1):
    tempC = float(input("Enter temperature in Celsius: "))
    tempF = tempC*(9/5) + 32
    print("The teperature in Farenheit is", tempF)
elif(choice==2):
    tempF = float(input("Enter the temperature in Farenheit: "))
    tempC = (tempF-32) * (5/9)
    print("The temperature in Celsius is", tempC)
else:
    print("Wrong choice entered!")
                        