class Day:

    def __init__(self, day_number, is_week):
        self.day_number = day_number
        self.is_week = is_week
        self.people = []
        self.day_fill = 0

    def __str__(self):
        return f"This day {self.day_number} with week # {self.is_week} has the following ppl working: \n{self.people}"

    def add_employee(self, employee): 
        self.people.append(employee.name)   
        self.day_fill += 1

        return self.day_fill

    def day_status(self):

        if self.day_fill >= 5:
            return False
        return True  
