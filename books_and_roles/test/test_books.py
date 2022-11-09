from http import HTTPStatus

from pythonProject.Repository_16.books_and_roles.api.books_api import BooksApi

def test_new_book_lifecycle(new_book):
    '''post new book - 1'''
    response = BooksApi().post_book(new_book)
    book_dict = response.json()
    first_book_id = book_dict['id']
    assert response.reason == 'Created'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'
    print('book id is: ' + f'{first_book_id}')

    '''check, that book was added - 2'''
    response = BooksApi().get_book(first_book_id)
    book_dict = response.json()
    assert book_dict == {'id': first_book_id, 'title': 'Anna Karenina', 'author': 'Lev Tolstoy'}
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

    '''check, that book is in the books list - 3'''
    response = BooksApi().get_all_books()
    all_books_dict = response.json()
    last_element = all_books_dict[-1]
    assert last_element == {'id': first_book_id, 'title': 'Anna Karenina', 'author': 'Lev Tolstoy'}, f'\n not in the list'

    '''update book title - 4'''
    new_title = {"title": "Katia Karenina"}
    response = BooksApi().put_book(first_book_id, new_title)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

    '''check, that book was updated - 5'''
    response = BooksApi().get_book(first_book_id)
    book_dict = response.json()
    assert book_dict == {'id': first_book_id, 'title': 'Katia Karenina', 'author': 'Lev Tolstoy'}
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

    '''check, that updated book is in the books list - 6'''
    response = BooksApi().get_all_books()
    all_books_dict = response.json()
    last_element = all_books_dict[-1]
    assert last_element == {'id': first_book_id, 'title': 'Katia Karenina', 'author': 'Lev Tolstoy'}, f'\n not in the list'

    '''check, that book was deleated - 7'''
    response = BooksApi().delete_book(first_book_id)
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'

def test_new_book_wrong_data(new_book_wrong_key):
    '''negative test - post new book with wrong key - 1'''
    response = BooksApi().post_book(new_book_wrong_key)
    assert response.reason == 'Bad Request'
    assert response.status_code == 400, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {400}'

def test_new_book_extra_key(new_book_missing_data):
    '''negative test - post new book with missing value - 1'''
    response = BooksApi().post_book(new_book_missing_data)
    assert response.reason == 'Bad Request'
    assert response.status_code == 400, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {400}'