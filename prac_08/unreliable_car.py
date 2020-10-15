from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{(super().__str__())}, Reliability: {self.reliability}"

    def start_fare(self):
        pass

    def drive(self, distance):
        """Drive like parent Car but use use reliability value to determine if drive succeeds or fails."""
        if randint(0, 100) <= self.reliability:
            # print("Success")
            distance_driven = super().drive(distance)
        else:
            # print("Fail")
            distance_driven = 0
        return distance_driven
