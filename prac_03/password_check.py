PASSWORD_MIN_LENGTH = 6


def main():
    password = get_password()
    print_masked_password(password)


def get_password():
    password = input("Password: ")
    while len(password) < PASSWORD_MIN_LENGTH:
        print(f"Password must be at least {PASSWORD_MIN_LENGTH} characters long.")
        password = input("Password: ")
    return password


def print_masked_password(password):
    print("*" * len(password))


main()
