from http import HTTPStatus

from pythonProject.Repository_16.books_and_roles.api.roles_api import RolesApi

def test_new_role_lifecycle(new_role):
    '''post new role - 1'''
    response = RolesApi().post_role(new_role)
    role_dict = response.json()
    first_role_id = role_dict['id']
    first_book_id = role_dict['book']
    assert response.reason == 'Created'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'
    print('role id is: ' + f'{first_role_id}')
    print('book id is: ' + f'{first_book_id}')

    '''check, that role was added - 2'''
    response = RolesApi().get_role(first_role_id)
    role_dict = response.json()
    assert role_dict == {"id": first_role_id, "name": "Anna Karenina", "type": "woman", 'level': 32, 'book': first_book_id}
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

    '''check, that role is in the roles list - 3'''
    response = RolesApi().get_all_roles()
    all_roles_dict = response.json()
    last_element = all_roles_dict[-1]
    assert last_element == {"id": first_role_id, "name": "Anna Karenina", "type": "woman", 'level': 32, 'book': first_book_id}, \
        f'\n not in the list'

    '''update role name - 4'''
    new_name = {"name": "Vania Karenin"}
    response = RolesApi().put_role(first_role_id, new_name)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

    '''check, that role was updated - 5'''
    response = RolesApi().get_role(first_role_id)
    role_dict = response.json()
    assert role_dict == {"id": first_role_id, "name": "Vania Karenin", "type": "woman", 'level': 32, 'book': first_book_id}
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

    '''check, that updated role is in the roles list - 6'''
    response = RolesApi().get_all_roles()
    all_roles_dict = response.json()
    last_element = all_roles_dict[-1]
    assert last_element == {"id": first_role_id, "name": "Vania Karenin", "type": "woman", 'level': 32, 'book': first_book_id}, \
        f'\n not in the list'

    '''check, that role was deleated - 7'''
    response = RolesApi().delete_role(first_role_id)
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'

def test_new_role_wrong_book(new_role_wrong_book):
    '''negative test - post new role with non-existing book - 8'''
    response = RolesApi().post_role(new_role_wrong_book)
    assert response.reason == 'Bad Request'
    assert response.status_code == 400, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {400}'