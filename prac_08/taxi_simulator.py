from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""

    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_option = input(">>> ").upper()
    while menu_option != "Q":
        if menu_option == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_option = int(input("Choose Taxi: "))
            current_taxi = taxis[taxi_option]
        elif menu_option == "D":
            try:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far?: "))
                current_taxi.drive(drive_distance)
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            except AttributeError:
                print("No taxi selected; please c)hoose a taxi first")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_option = input(">>> ").upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display each taxi in taxi list."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
