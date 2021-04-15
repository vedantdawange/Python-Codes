#A program in python to print sum of all numbers in given range
ll=int(input("Enter the lower limit"))
ul=int(input("Enter upper limit"))

#While
sum=0
i=ll
while i<=ul:
    sum=sum+i
    i=i+1
print("Using the while:",sum)


#Do While
sum=0
i=ll
while True:
    if i>ul:
        break
    else:
        sum=sum+i
        i=i+1
print("Using The Do While:",sum)

