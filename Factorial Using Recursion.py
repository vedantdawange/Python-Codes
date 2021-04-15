#Recurcion Factorial
def factorial(a):
    if a==1:
        return 1
    return(a*factorial(a-1))


a=int(input("Enter The Number"))
ans=factorial(a)
print("Factorial of ",a,"is",ans)
