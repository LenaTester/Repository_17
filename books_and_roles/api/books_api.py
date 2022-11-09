from pythonProject.Repository_16.books_and_roles.api.base_api import BaseAPI

class BooksApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_url = "/books/"

    def post_book(self, new_book):
        return self.post(url=f"{self.user_url}", json=new_book)

    def get_book(self, book_id, headers=None):
        return self.get(url=f"{self.user_url}{book_id}")

    def get_all_books(self, headers=None):
        return self.get(url=f"{self.user_url}")

    def put_book(self, book_id, new_title):
        return self.put(url=f"{self.user_url}{book_id}", json=new_title)

    def delete_book(self, book_id):
        return self.delete(url=f"{self.user_url}{book_id}")