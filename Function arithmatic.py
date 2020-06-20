# Write a program to do arithmatic operation using function
def sumnum(a, b):
    ans = a + b
    print("Addition is :", ans)


def subtraction(a, b):
    ans = a - b
    print("Subtraction is :", ans)


def division(a, b):
    ans = a / b
    print("Division is :", ans)


def multiply(a, b):
    ans = a * b
    print("Multiplication is :", ans)


while True:
    a = float(input("Enter Your First Number: "))
    b = float(input("Enter Your Second Number: "))
    ch = input("Enter Your Choice: \n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division")
    if ch == '1':
        sumnum(a, b)
    elif ch == '2':
        subtraction(a, b)
    elif ch == '3':
        multiply(a, b)
    elif ch == '4':
        division(a, b)
    else:
        print("Please Enter a Valid Choice")

    cont = input("Do You wish to Continue?(Y/N) : ")
    if cont == 'n' or cont == 'N':
        break
