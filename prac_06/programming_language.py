class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_dynamic()}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if a ProgrammingLanguage is dynamically typed."""
        return self.typing == "Dynamic"
