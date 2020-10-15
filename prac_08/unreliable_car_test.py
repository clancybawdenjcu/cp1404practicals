from prac_08.unreliable_car import UnreliableCar


def main():
    """Demo test code to learn inheritance."""
    test_car = UnreliableCar("Holden", 200, 30)
    test_car.drive(40)
    print(test_car)
    test_car.drive(80)
    print(test_car)
    test_car2 = UnreliableCar("Ford", 200, 70)
    test_car2.drive(40)
    print(test_car2)
    test_car2.drive(80)
    print(test_car2)


main()
