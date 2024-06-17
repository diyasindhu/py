# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
choice = int(input("Enter 1 for addition(+)\n\
Enter 2 for subtraction(-)\n\
Enter 3 for multiplication(x)\n\
Enter 4 for division(/):\n"))
if(choice == 1):
    ans = num1 + num2
    print("Addition of", num1, "and", num2, "=", ans)
elif(choice == 2):
    ans = num1-num2
    print("Difference of", num1, "and", num2, "=", ans)
elif(choice==3):
    ans = num1*num2
    print("Multiplication of", num1, "and", num2, "=", ans)
elif(choice==4):
    ans = num1/num2
    print("Division of", num1, "and", num2, "=", ans)
else:
    print("Wrong choice entered!")