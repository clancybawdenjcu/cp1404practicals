import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6

number_quick_picks = int(input("How many quick picks?: "))
numbers = []

for quick_pick in range(number_quick_picks):
    while len(numbers) != NUMBERS_PER_QUICK_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers = sorted(numbers)
    print(f"{numbers[0]:2} {numbers[1]:2} {numbers[2]:2} {numbers[3]:2} {numbers[4]:2} {numbers[5]:2}")
    numbers.clear()
