# Write a python program that removes all punctuation from a given string
string = input("ENter a string to remove all punctuation from it: ")
list1 = list(string)
string=""
for i in list1:
    if((i>='A' and i<='Z') or (i>='a' and i<='z') or (i>='0' and i<='9')):
        string=string+i
print(string)