import pandas as pd
from sys import argv
from employees import Employee
from week import Week
from days import Day


class Load_data:

    def load_employees(self):
        """
        Loads employee data
        """
        df = pd.read_csv('emp_data2.csv', index_col=0)

        employees = []

        for i in df.columns:
            my_list = list(df[i])
            new_list = list(filter(lambda num: num != 'FALSE', my_list))
            employee = Employee(i, new_list)
            employees.append(employee)
            
        return employees

    def load_weeks(self):
        """
        Loads work weeks in month
        """

        weeks_in_month = []

        df2 = pd.read_csv('month_data.csv')
        for j in df2.columns:
            sep_week = Week(j, list(df2[j]))
            weeks_in_month.append(sep_week)

        return weeks_in_month

    def load_days(self):

        days_in_weeks = []

        df3 = pd.read_csv('month_data.csv')

        for j in df3.columns:
            for k in df3[j]:
                sep_day = Day(k, j)
                days_in_weeks.append(sep_day)

        return days_in_weeks            




