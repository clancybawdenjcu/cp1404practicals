PASSWORD_MIN_LENGTH = 6

password = input("Password: ")
while len(password) < PASSWORD_MIN_LENGTH:
    print(f"Password must be at least {PASSWORD_MIN_LENGTH} characters long.")
    password = input("Password: ")
print("*" * len(password))
