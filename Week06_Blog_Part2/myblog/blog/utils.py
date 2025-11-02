from faker import Faker
from django.contrib.auth.models import User
from blog.models import Post, Comment
import random

fake = Faker()

def create_fake_data():
    print("✅ Creating random users...")

    # ✅ Step 1: Create multiple random users
    users = []
    for _ in range(5):   # how many users you want
        username = fake.user_name()

        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password("password123")
            user.save()

        users.append(user)

    print(f"✅ {len(users)} users ready!")

    # ✅ Step 2: Create posts with random user
    print("✅ Creating posts with random users...")

    posts = []
    for _ in range(10):   # number of posts
        author = random.choice(users)   # pick random user

        post = Post.objects.create(
            user=author,
            title=fake.sentence(),
            content=fake.paragraph()
        )
        posts.append(post)

    print("✅ 10 posts created!")

    # ✅ Step 3: Random comments from random users
    print("✅ Creating comments...")

    for post in posts:
        for _ in range(random.randint(1, 5)):  # 1–5 comments
            commenter = random.choice(users)

            Comment.objects.create(
                post=post,
                user=commenter,
                content=fake.sentence()
            )

    print("🎉 All fake users, posts, and comments created successfully!")
