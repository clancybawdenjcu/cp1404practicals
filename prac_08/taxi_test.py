from prac_08.taxi import Taxi


def main():
    """Demo test code to learn inheritance."""
    prius_1 = Taxi("Prius 1", 10)
    prius_1.drive(40)
    print(prius_1)
    prius_1.start_fare()
    prius_1.drive(100)
    print(prius_1)


main()
