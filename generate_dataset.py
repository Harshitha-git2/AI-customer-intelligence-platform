from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

os.makedirs("data", exist_ok=True)

cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune"
]

products = [
    "Laptop",
    "Phone",
    "Watch",
    "Headphones",
    "Camera",
    "Tablet"
]

data = []

for i in range(500):

    income = random.randint(20000,150000)
    spending = random.randint(1,100)
    tenure = random.randint(1,60)

    churn = 1 if tenure < 12 and spending < 40 else 0

    data.append([
        i+1,
        fake.name(),
        random.randint(18,60),
        random.choice(["Male","Female"]),
        random.choice(cities),
        income,
        spending,
        tenure,
        random.choice(products),
        churn
    ])

df = pd.DataFrame(data, columns=[
    "customer_id",
    "name",
    "age",
    "gender",
    "city",
    "income",
    "spending_score",
    "tenure",
    "favorite_product",
    "churn"
])

df.to_csv("data/customers.csv", index=False)

print("Dataset Created Successfully")