#write a program to persorm swap operaton on 2 variables
a= int(input("Entrer First number :"))
b= int(input("Enter Second Number :"))
#printing without 3rd variable
print("Printing without 3rd variable")
a=a+b
b=a-b
a=a-b
print("The Value after swaping:",a,b)
