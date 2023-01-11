"""
Write a python script to print first "N" odd natural numbers in reverse order
"""

# taking a values from the user
n = int(input("Enter a number : "))

# printing first "n" odd natural numbers in reverse order using while loop
while n >= 1 :
    print(n*2-1, end=' ')
    n -= 1