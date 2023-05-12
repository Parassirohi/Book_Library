
import random
from faker import Faker

from .models import Book

fake = Faker()

for i in range(100):
    title = fake.sentence(nb_words=random.randint(1, 5))
    author = fake.name()
    publisher = fake.company()
    publication_year = fake.year()
    number_of_copies = random.randint(1, 10)
    number_of_available_copies = random.randint(0, number_of_copies)
    book = Book(title=title, author=author, publisher=publisher, publication_year=publication_year,
                number_of_copies=number_of_copies, number_of_available_copies=number_of_available_copies)
    book.save()



