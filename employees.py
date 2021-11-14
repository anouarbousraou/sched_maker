
class Employee:

    def __init__(self, name, availability):
        self.name = name
        self.availability = availability
        self.week_count = 0
        self.meets = 0

    def __str__(self):
        return f"name: {self.name}, is available: \n{self.availability}"

    def was_added(self):
        self.week_count += 1

        if self.week_count > 3:
            return False

    def add_unique_met(self):
        self.meets += 1

        

        


