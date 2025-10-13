from .models import Feedback
from faker import Faker
import random

faker = Faker()

def create_data(n=50):
    for _ in range(n):
        Feedback.objects.create(
            name=faker.name(),
            email=faker.email(),
            rating=random.randint(1, 5),
            message=faker.text(max_nb_chars=200)
        )
    print("✅ Fake feedback data created successfully!")
