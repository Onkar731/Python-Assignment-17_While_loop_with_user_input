"""
Write a python script to print first "N" natural numbers in reverse order
"""

# taking a values from the user
n = int(input("Enter a number : "))

# printing first "n" natural numbers in reverse order using while loop
while n >= 1 :
    print(n, end=' ')
    n -= 1