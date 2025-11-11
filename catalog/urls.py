from django.urls import path

from catalog.views import (
    index,
    about,
    LiteraryFormatListView,
    BookListView,
    AuthorListView,
    AuthorDetailView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    LiteraryFormatCreateView,
    LiteraryFormatUpdateView,
    LiteraryFormatDeleteView,
    AuthorCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("literary-formats/create/", LiteraryFormatCreateView.as_view(), name="literary-format-create"),
    path("literary-formats/<int:pk>/update/", LiteraryFormatUpdateView.as_view(), name="literary-format-update"),
    path("literary-formats/<int:pk>/delete/", LiteraryFormatDeleteView.as_view(), name="literary-format-delete"),
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/create/", BookCreateView.as_view(), name="books-create"),
    path("books/<int:pk>", BookDetailView.as_view(), name="books-detail"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="books-update"),
    path("authors/", AuthorListView.as_view(), name="authors-list"),
    path("authors/create/", AuthorCreateView.as_view(), name="authors-create"),
    path("authors/<int:pk>", AuthorDetailView.as_view(), name="authors-detail"),
    path("about/", about, name="about"),
]

app_name = "catalog"