"""
Write a python script to print first N natural numbers
"""

# taking a values from the user
n = int(input("Enter a number : "))

# defining a counter variable for iteration
i = 1

# printing first "n" natural numbers using while loop
while i <= n :
    print(i, end=' ')
    i += 1