import pytest

from pythonProject.Repository_16.books_and_roles.api.books_api import BooksApi

@pytest.fixture
def new_book():
    return {"title": "Anna Karenina", "author": "Lev Tolstoy"}

@pytest.fixture
def new_role(new_book):
    response = BooksApi().post_book(new_book)
    book_dict = response.json()
    first_book_id = book_dict['id']
    return {"name": "Anna Karenina", "type": "woman", 'level': '32', 'book': first_book_id}

@pytest.fixture
def new_book_wrong_key():
    return {"name": "Anna Karenina", "author": "Lev Tolstoy"}

@pytest.fixture
def new_book_missing_data():
    return {"title": "", "author": "Lev Tolstoy"}

@pytest.fixture
def new_role_wrong_book():
    return {"name": "Anna Karenina", "type": "woman", 'level': '32', 'book': 10000}