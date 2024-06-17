# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
str = input("Enter your message: ")
lines = [str]
while(str!=""):
    str=input("Enter your message: ")
    lines.append(str)
print("Entered lines are:")
for i in lines:
    print(i)