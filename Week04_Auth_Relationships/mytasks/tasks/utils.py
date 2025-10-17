from faker import Faker
from django.contrib.auth.models import User
from .models import Task

faker = Faker()

def create_demo_data(n=50):
    """
    Create 'n' fake tasks for the admin user.
    """

    try:
        admin_user = User.objects.get(username="admin")
    except User.DoesNotExist:
        print("❌ Admin user not found! Create admin user first using:")
        print("   python manage.py createsuperuser")
        return

    for _ in range(n):
        Task.objects.create(
            user=admin_user,
            title=faker.sentence(nb_words=5),
            description=faker.paragraph(nb_sentences=3),
            completed=faker.boolean(chance_of_getting_true=40), 
        )

    print(f"✅ {n} fake tasks created for admin user!")
