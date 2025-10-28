from django.contrib.auth.models import User
from .models import Post  # apne app ka naam replace kar le
from faker import Faker
import random

fake = Faker()

users = list(User.objects.all())


def demo_data(n=50):
    for _ in range(n):
        user = random.choice(users)
        post = Post.objects.create(
            user=user,
            title=fake.sentence(nb_words=6),
            content=fake.paragraph(nb_sentences=5)
        )
        print(post.title)
