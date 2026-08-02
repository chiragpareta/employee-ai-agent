import os
import random
from faker import Faker
import pandas as pd

fake = Faker()

DEPARTMENTS = [
    "Engineering",
    "Sales",
    "Marketing",
    "Finance",
    "HR",
    "Operations",
    "Customer Support",
    "IT"
]


class CSVTool:

    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True )

    def generate_employee_csv(self, rows=20):

        employees = []

        for i in range(1, rows + 1):

            employees.append(
                {
                    "Employee ID": f"EMP{i:03}",
                    "Name": fake.name(),
                    "Department": random.choice(DEPARTMENTS),
                    "Email": fake.email(),
                    "Salary": random.randint(50000, 120000),
                    "Joining Date": fake.date_between(
                        start_date="-8y",
                        end_date="today"
                    ),
                    "City": fake.city()
                }
            )

        df = pd.DataFrame(employees)

        csv_path = os.path.join(
            self.output_dir,
            "employees.csv"
        )

        df.to_csv(csv_path, index=False)

        return csv_path