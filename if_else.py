
# Assign a numeric value

import sys

number = int(sys.argv[1])
#number = 70

# Check the is more than 70 or not
if (number >= 70):
    print("You have passed")
else:
    print("You have not passed")



# Python program to demonstrate
# command line arguments


'''
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
    
print("\n\nResult:", Sum)
'''