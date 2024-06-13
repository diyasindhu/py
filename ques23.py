n=int(input("enter the temp "))
def temprature(temp):
    celsius=(temp-32)*(5/9)
    return(celsius)
print(temprature(n))