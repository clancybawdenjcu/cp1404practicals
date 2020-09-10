def main():
    email = input("Enter email: ").strip()
    name_email_dict = {}
    while email != "":
        name = get_name(email).title()
        is_name_correct = input(f"Is your name {name}? (Y/N): ").upper()
        if is_name_correct == "Y":
            name_email_dict[name] = email
        else:
            name = input("Name: ")
            name_email_dict[name] = email
        email = input("Enter email: ").strip()

    # for name in name_email_dict:
    #     print(f"{name} {name_email_dict[name]}")

    for name in name_email_dict:
        print(name_email_dict.items())


def get_name(email):
    email_parts = email.split("@")
    return " ".join(email_parts[0].split("."))


main()
