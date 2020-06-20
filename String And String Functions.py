# String Functions


# Length of String
print("Length of String")
x = input("Enter the String:")
c = 0
for i in x:
    c = c + 1
print("Length of the string is: ", c)

# concatenate
print("\nConcatenate Strings")
x = input("Enter the String:")
y = input("Enter String 2 : ")
z = ""
for i in x:
    z += str(i)
for i in y:
    z += str(i)
print("The concatenated string is: ", z)

# Reverse of string
print("\nReverse of string:")
x = input("Enter the String:")
rev = x[::-1]
print("The reverse of the string is: ", rev)

# compare
print("\nComparing string")
a = input("Enter First String: ")
b = input("Enter Second String: ")
c = 0

if len(a) == len(b):
    for i in range(len(a)):
        if a[i] == b[i]:
            c = c + 1
if c == len(a):
    print("The Strings are Equal: ")
else:
    print("The Strings are not Equal! ")

# Find Sub String
print("\nFinding Substring")
s1 = input("Enter the string: ")
s2 = input("Enter the string to be searched: ")

if s2 in s1:
    print("Substring Exists")
else:
    print("Substring does not exist")

# Palindrome
print("\nPalindrome")
a = input("Enter the string: ")
rev = a[::-1]
if a == rev:
    print("The String is a Palindrome String!")
else:
    print("The string is not a Palindrome String!")
