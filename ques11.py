def generateFibo(n):
    if n<=0:
        return []
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    fibo=[0,1]
    for i in range(2,n):
        nextNum=fibo[-1]+fibo[-2]
        fibo.append(nextNum)
    return fibo    

n=int(input("enter the nth number of the sequence"))
fibo=generateFibo(n)
print("The first ",n," numbers of the fibo sequence are: ")
print(fibo)
