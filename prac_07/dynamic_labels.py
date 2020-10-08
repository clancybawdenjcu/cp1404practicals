from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Bob", "James", "Michelle", "Clint", "Andy", "Barry", "Cassie"]


class DynamicLabels(App):
    """Kivy app to dynamically display list of names as labels."""

    def build(self):
        """Build kivy app from .kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def on_start(self):
        """Create name label widgets on program start."""
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.name_labels.add_widget(temp_label)


DynamicLabels().run()
