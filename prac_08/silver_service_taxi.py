from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi."""
    FLAGFALL = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise an SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{(super().__str__())} plus flagfall of ${self.FLAGFALL:.2f}."

    def get_fare(self):
        """Get fare, adding flagfall charge."""
        return super().get_fare() + self.FLAGFALL
