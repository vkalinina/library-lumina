# 📚 Library Management System

A Django-based web application for managing books, authors, and literary formats. This project demonstrates CRUD operations, user authentication, search functionality, and clean MVT architecture.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-4.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **User Authentication**: Secure login/logout system with custom user model
- **Author Management**: Authors extend Django's User model with pseudonyms and birthdays
- **Book Catalog**: Comprehensive book management with pricing and format categorization
- **Literary Formats**: Organize books by genres and formats
- **Search Functionality**: Quick book search by title
- **Pagination**: Efficient browsing with paginated book lists
- **CRUD Operations**: Full Create, Read, Update, Delete functionality for all entities
- **Session Tracking**: Visit counter to track user activity

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-management.git
   cd library-management
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Populate database with sample data**
   ```bash
   python manage.py populate_db
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Demo credentials: `username: demo` / `password: demo123`

## 📁 Project Structure

```
library-management/
├── catalog/                    # Main application
│   ├── management/
│   │   └── commands/
│   │       └── populate_db.py  # Database population script
│   ├── migrations/
│   ├── templates/
│   │   └── catalog/
│   ├── models.py               # Data models
│   ├── views.py                # View logic
│   ├── forms.py                # Form definitions
│   └── urls.py                 # URL routing
├── static/                     # Static files (CSS, JS, images)
├── templates/                  # Base templates
├── manage.py
├── requirements.txt
└── README.md
```

## 💾 Database Schema

### Models

**Author** (extends AbstractUser)
- username (primary identifier)
- first_name, last_name
- pseudonym (optional)
- birthday (optional)
- Standard User fields (email, password, etc.)

**Book**
- title
- price (Decimal)
- format (ForeignKey to LiteraryFormat)
- author (ManyToMany with Author)

**LiteraryFormat**
- name (e.g., Novel, Poetry, Drama)

## 🎯 Key Functionality

### Views

- **Index**: Dashboard showing statistics and visit counter
- **Book List**: Paginated list with search functionality
- **Book Detail**: Detailed view of individual books
- **CRUD Operations**: Create, update, and delete books, authors, and formats
- **Search**: Filter books by title

### Authentication

All views require user authentication using Django's `LoginRequiredMixin` and `@login_required` decorator.

## 🛠️ Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Authentication**: Django's built-in auth system
- **Forms**: Django Forms with custom validation
- **Templates**: Django Template Language

## 📝 Management Commands

### Populate Database
```bash
python manage.py populate_db
```
Creates sample data including:
- 5 famous authors (J.K. Rowling, George Orwell, Jane Austen, etc.)
- 10 literary formats
- 10+ books
- 1 demo user for testing

## 🔐 Default Credentials

**Demo User** (created by `populate_db`):
- Username: `demo`
- Password: `demo123`

**Sample Authors** (all with password `password123`):
- jk_rowling
- george_orwell
- jane_austen
- mark_twain
- agatha_christie

## 🚀 Deployment

This project is ready for deployment on platforms like:
- Heroku
- Railway
- PythonAnywhere
- DigitalOcean

Remember to:
1. Set `DEBUG = False` in production
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for sensitive data
4. Switch to PostgreSQL for production database
5. Configure static files with WhiteNoise or similar

## 📈 Future Enhancements

- [ ] Book reviews and ratings
- [ ] Advanced filtering (by author, format, price range)
- [ ] Book cover image upload
- [ ] Reading lists and favorites
- [ ] Export to CSV/PDF
- [ ] REST API with Django REST Framework
- [ ] Frontend with React or Vue.js

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Viktoria Kalinina**
- GitHub: [@vkalinina](https://github.com/vkalinina/)
- LinkedIn: [viktoria-kalinina-7ab10636a](https://linkedin.com/in/viktoria-kalinina-7ab10636a)

## 🙏 Acknowledgments

- Django Documentation
- Python Community
- All contributors to open-source libraries used in this project

---

⭐ If you find this project useful, please consider giving it a star!
