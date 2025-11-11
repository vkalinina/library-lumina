from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from catalog.models import LiteraryFormat, Book

User = get_user_model()


class Command(BaseCommand):
    help = "Populate database with sample literary data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting database population..."))

        # Create Literary Formats
        formats_data = [
            "Novel",
            "Short Story",
            "Poetry",
            "Essay",
            "Drama",
            "Biography",
            "Memoir",
            "Science Fiction",
            "Fantasy",
            "Mystery",
        ]

        formats = []
        for format_name in formats_data:
            format_obj, created = LiteraryFormat.objects.get_or_create(
                name=format_name
            )
            formats.append(format_obj)
            if created:
                self.stdout.write(f"Created format: {format_name}")

        # Create Authors (Users)
        authors_data = [
            {
                "username": "jk_rowling",
                "first_name": "Joanne",
                "last_name": "Rowling",
                "pseudonym": "J.K. Rowling",
                "birthday": "1965-07-31",
                "email": "jkrowling@example.com",
            },
            {
                "username": "george_orwell",
                "first_name": "Eric",
                "last_name": "Blair",
                "pseudonym": "George Orwell",
                "birthday": "1903-06-25",
                "email": "orwell@example.com",
            },
            {
                "username": "jane_austen",
                "first_name": "Jane",
                "last_name": "Austen",
                "pseudonym": None,
                "birthday": "1775-12-16",
                "email": "jausten@example.com",
            },
            {
                "username": "mark_twain",
                "first_name": "Samuel",
                "last_name": "Clemens",
                "pseudonym": "Mark Twain",
                "birthday": "1835-11-30",
                "email": "mtwain@example.com",
            },
            {
                "username": "agatha_christie",
                "first_name": "Agatha",
                "last_name": "Christie",
                "pseudonym": None,
                "birthday": "1890-09-15",
                "email": "achristie@example.com",
            },
        ]

        authors = []
        for author_data in authors_data:
            author, created = User.objects.get_or_create(
                username=author_data["username"],
                defaults={
                    "first_name": author_data["first_name"],
                    "last_name": author_data["last_name"],
                    "pseudonym": author_data["pseudonym"],
                    "birthday": author_data["birthday"],
                    "email": author_data["email"],
                },
            )
            if created:
                author.set_password("password123")
                author.save()
                self.stdout.write(f"Created author: {author.username}")
            authors.append(author)

        # Create Books
        books_data = [
            {
                "title": "Harry Potter and the Philosopher's Stone",
                "price": Decimal("29.99"),
                "format": "Fantasy",
                "authors": ["jk_rowling"],
            },
            {
                "title": "1984",
                "price": Decimal("19.99"),
                "format": "Novel",
                "authors": ["george_orwell"],
            },
            {
                "title": "Animal Farm",
                "price": Decimal("15.99"),
                "format": "Novel",
                "authors": ["george_orwell"],
            },
            {
                "title": "Pride and Prejudice",
                "price": Decimal("12.99"),
                "format": "Novel",
                "authors": ["jane_austen"],
            },
            {
                "title": "The Adventures of Tom Sawyer",
                "price": Decimal("14.99"),
                "format": "Novel",
                "authors": ["mark_twain"],
            },
            {
                "title": "Murder on the Orient Express",
                "price": Decimal("18.99"),
                "format": "Mystery",
                "authors": ["agatha_christie"],
            },
            {
                "title": "And Then There Were None",
                "price": Decimal("17.99"),
                "format": "Mystery",
                "authors": ["agatha_christie"],
            },
            {
                "title": "Emma",
                "price": Decimal("13.99"),
                "format": "Novel",
                "authors": ["jane_austen"],
            },
            {
                "title": "Harry Potter and the Chamber of Secrets",
                "price": Decimal("29.99"),
                "format": "Fantasy",
                "authors": ["jk_rowling"],
            },
            {
                "title": "The Adventures of Huckleberry Finn",
                "price": Decimal("16.99"),
                "format": "Novel",
                "authors": ["mark_twain"],
            },
        ]

        for book_data in books_data:
            format_obj = LiteraryFormat.objects.get(name=book_data["format"])
            book, created = Book.objects.get_or_create(
                title=book_data["title"],
                defaults={
                    "price": book_data["price"],
                    "format": format_obj,
                },
            )
            if created:
                # Add authors to the book
                for author_username in book_data["authors"]:
                    author = User.objects.get(username=author_username)
                    book.author.add(author)
                self.stdout.write(f"Created book: {book.title}")

        # Create a demo user for login
        demo_user, created = User.objects.get_or_create(
            username="demo",
            defaults={
                "first_name": "Demo",
                "last_name": "User",
                "email": "demo@example.com",
            },
        )
        if created:
            demo_user.set_password("demo123")
            demo_user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    "\n" + "="*50 +
                    "\nDemo user created!"
                    "\nUsername: demo"
                    "\nPassword: demo123"
                    "\n" + "="*50
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"\n✓ Database populated successfully!"
                f"\n✓ Total Authors: {User.objects.count()}"
                f"\n✓ Total Books: {Book.objects.count()}"
                f"\n✓ Total Formats: {LiteraryFormat.objects.count()}"
            )
        )
