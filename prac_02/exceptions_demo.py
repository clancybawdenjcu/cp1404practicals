"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot have denominator value of '0', please try again.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Question 1:
# When a non-integer value (i.e. "a", or "1.123") is entered into the input prompt.

# Question 2:
# When the denominator input entered is "0".

# Question 3:
# Yes; use a while loop to check if "0" is entered as a denominator value. If it is, prompt for a new denominator value
# to be entered.
