from faker import Faker
from sqlalchemy.orm import Session
from app.models import Employee
import random

faker = Faker()
departments = ["HR", "Engineering", "Sales", "Marketing", "Finance"]

def generate_fake_employees(db: Session, count: int = 100):
    for _ in range(count):
        employee =Employee(
            name=faker.name(),
            email=faker.unique.email(),
            department=random.choice(departments),
            salary=round(random.uniform(30000, 120000), 2),
            city=faker.city()
        )
        db.add(employee)
    db.commit()