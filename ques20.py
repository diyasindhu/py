n = int (input ("Enter number of elements: ")) 
list1 = []
for i in range (n):
    x = int(input())
    list1.append(x)
print("List is :", list1)

total = 0

for ele in range(0, len(list1)):
	total = total + list1[ele]

print("Sum of all elements in given list: ", total)