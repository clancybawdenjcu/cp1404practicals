from prac_06.guitar import Guitar


def main():

    print("My guitars!")
    guitars = []  # Create empty guitars list.

    guitars.append(Guitar("Fender Stratocaster", 2014, 16035.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 765.4))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitar_name = input("Name: ").title()
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar_to_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.\n")
        guitar_name = input("Name: ").title()

    print("These are my guitars:")
    for count, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {count + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
