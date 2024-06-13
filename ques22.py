list1=[1,2,3,4,5,6]
large=list1[0]
small=list1[0]
for num in list1:
    if(num>large):
        large=num
    elif(num<small):
        small=num
print("the largest number in list is ",large)
print("the smallest num in the list is ",small)