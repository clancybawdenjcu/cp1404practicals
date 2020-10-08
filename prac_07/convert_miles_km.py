from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KMS = 1.60934


class ConvertMilesToKms(App):
    """Kivy App for converting miles to kilometres."""
    output_kms = StringProperty()

    def build(self):
        """Build kivy app from .kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Handle converting miles to kilometres."""
        miles = self.convert_to_number(text)
        self.output_kms = str(miles * FACTOR_MILES_TO_KMS)

    def handle_increment(self, text, change):
        """Handle increasing or decreasing input_miles value by one."""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod  # Had to refer to the solution for this - I wasn't otherwise able to convert str to float.
    def convert_to_number(text):
        """Convert number to float type, or return 0.0 if number isn't passed in."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesToKms().run()
