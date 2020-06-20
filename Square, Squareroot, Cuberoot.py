num=int(input("Enter Your Number"))
if num<10:
    ans=num**2
    print(ans)
elif num<100:
    ans=num**(1/2)
    print(ans)
elif num<1000:
    ans=num**(1/3)
    print(ans)
else:
    print("Invalid Number!")
