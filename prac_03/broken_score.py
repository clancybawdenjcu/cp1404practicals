"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    # score = float(input("Enter score: "))
    # while score < 0 or score > 100:
    #     print("Invalid score")
    #     score = float(input("Enter score: "))
    score = random.randint(0, 100)
    result = get_result(score)
    print(f"Score: {score:>10}.")
    print(f"Result: {result:>9}.")


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
