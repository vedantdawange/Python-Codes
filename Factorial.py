#Factorial of a Number
n=int(input("Enter The number : "))
fact=1

if n<0:
    print("Invalid number")
elif n==0 or n==1:
    print(fact)
else:
#assending
    i=1
    while i<=n:
      fact=fact*i
      i=i+1
    print(fact)
#decendings
    i=n
    fact=1
    while i>=1:
       fact=fact*i
       i=i-1
    print(fact)
