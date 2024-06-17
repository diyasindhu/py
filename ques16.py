# Write a program in python that counts the frequency of each character in a string.
str = input("Enter a string to count the frequency of each character: ")
unique = []
for i in str:
    if(unique.count(i)==0):
        unique.append(i)
for i in unique:
    print("The frequency of character", i, "is", str.count(i))