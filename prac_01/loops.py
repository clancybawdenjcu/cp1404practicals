# Question 3
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question 3a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Question 3b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Question 3c
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print("\n")

# Question 3d
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*" * i)
