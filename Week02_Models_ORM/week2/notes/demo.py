
from faker import Faker
from notes.models import Note

fake = Faker()
def Create_data(n = 50):
    for _ in range(n):
        Note.objects.create(
            title=fake.sentence(nb_words=5),
            content=fake.paragraph(nb_sentences=5),
        )

    print("✅ Data created successfully")
