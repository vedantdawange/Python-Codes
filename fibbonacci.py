#Fibbonacci
n=int(input("Enter The number of elements : "))
#limit=int(input("Enter the upper limit : "))
#Printing number of elements
a=0
b=1
i=3
print(a)
print(b)
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1
'''
print("\n")
#Printing timm the upper limit
a=0
b=1
i=3
print(a)
print(b)
while True:
    c=a+b
    if c>limit:
        break
    else:
        print(c)
        a=b
        b=c
        i=i+1
print("Those were '",i-1,"' elements")
'''