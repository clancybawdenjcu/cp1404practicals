# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
name = input("What is your name?:")
out_file = open("name.txt", "w")
print(f"{name}", file=out_file)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
in_file = open("name.txt")
print(f"Your name is {in_file.readline()}")
in_file.close()

# 3. Write code that opens "numbers.txt", reads only the first two numbers, adds them together, then prints the result.
NUMBER_OF_LINES_TO_CALC = 2
total = 0
in_file = open("numbers.txt", "r")
for i in range(NUMBER_OF_LINES_TO_CALC):
    value = int(in_file.readline())
    total += value
print(total)

# 4. write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of
# numbers.
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += float(line)
print(total)
