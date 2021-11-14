
class Week:

    def __init__(self, week_number, has_days):
        self.week_number = week_number
        self.has_days = has_days
        self.employees_in_week = []

    def add_emp_to_week(self, employee):
        self.employees_in_week.append(employee)
        
