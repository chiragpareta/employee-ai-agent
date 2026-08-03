from faker import Faker
import pandas as pd
import random

fake = Faker()

CSV_PATH = "output/employees.csv"

DEPARTMENTS = [
    "Engineering",
    "Sales",
    "Marketing",
    "Finance",
    "HR",
]

def generate_csv():
    employees = []

    for i in range(20):
        employees.append({
            "Employee ID": f"EMP{i+1:03}",
            "Name": fake.name(),
            "Department": random.choice(DEPARTMENTS),
            "Email": fake.email(),
            "Salary": random.randint(50000, 120000),
        })

    df = pd.DataFrame(employees)
    df.to_csv(CSV_PATH, index=False)

    return CSV_PATH