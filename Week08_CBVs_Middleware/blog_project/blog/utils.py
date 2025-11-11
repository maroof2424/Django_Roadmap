from faker import Faker
from .models import Post

faker = Faker()

def create_demo_posts(n = 20):
    for _ in range(n):
        try:
            title = faker.sentence(),
            content = faker.paragraph(nb_sentences=5)
            Post.objects.create(
                title=title,
                content=content,
            )
        except Exception as e:
            print(e)
    print(f"{n} Post Created")