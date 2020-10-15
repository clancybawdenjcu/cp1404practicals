from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Demo test code to learn inheritance."""
    test_taxi = SilverServiceTaxi("Mercedes", 24, 2)
    test_taxi.drive(18)
    print(test_taxi)
    print(f"Fare: ${test_taxi.get_fare():.2f}")
    test_taxi.start_fare()
    test_taxi.drive(18)
    print(test_taxi)
    print(f"Fare: ${test_taxi.get_fare():.2f}")
    test_taxi2 = SilverServiceTaxi("Hummer", 120, 4)
    test_taxi2.drive(40)
    print(test_taxi2)
    print(f"Fare: ${test_taxi2.get_fare():.2f}")


main()
