import employees
import load_data
import random

reader = load_data.Load_data()
employees = reader.load_employees()
weeks = reader.load_weeks()
days = reader.load_days()


def make_calendar():

    for week in weeks:
        for day in days:
            if day.day_number in week.has_days:
                while day.day_status():
                    employee = random.choice(employees) 
                    if day.day_number in employee.availability:
                        day.add_employee(employee)
                        week.add_emp_to_week(employee.name)

def count_unique_meets():
    make_calendar()

    my_dict = {'week_1': [], 'week_2': [], 'week_3': [], 'week_4': []}
    for day in days:
        my_dict[day.is_week].append(day)

    counter = []
    for k, v in my_dict.items():
        total_days = []
        print(f'this is week {k}')
        for i in v:
            total_days += i.people
        print(total_days)

            

count_unique_meets()