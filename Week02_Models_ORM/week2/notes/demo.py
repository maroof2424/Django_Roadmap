import os
import sys
import django
from faker import Faker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "week2.settings")

django.setup()

from notes.models import Note

fake = Faker()
for _ in range(50):
    Note.objects.create(
        title=fake.sentence(nb_words=5),
        content=fake.paragraph(nb_sentences=5),
    )

print("✅ Data created successfully")
