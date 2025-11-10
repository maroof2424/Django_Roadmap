from faker import Faker
import random
from .models import Product, Order

fake = Faker()

def create_fake_products(n=10):
    """
    Create n fake products in the database
    """
    for _ in range(n):
        Product.objects.create(
            title=fake.word().title(),
            price=round(random.uniform(100, 5000), 2),
            description=fake.text(),
            image="https://png.pngtree.com/thumb_back/fh260/background/20230718/pngtree-d-rendered-image-web-or-mobile-application-for-ecommerce-with-paper-image_3911610.jpg"  # default image for dev
        )
    return f"{n} fake products created!"

def create_fake_orders(n=10):
    """
    Create n fake orders in the database
    """
    for _ in range(n):
        Order.objects.create(
            name=fake.name(),
            email=fake.email(),
            address=fake.address(),
            total_price=round(random.uniform(500, 20000), 2)
        )
    return f"{n} fake orders created!"
