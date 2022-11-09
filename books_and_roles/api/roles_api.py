from pythonProject.Repository_16.books_and_roles.api.base_api import BaseAPI

class RolesApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_url = "/roles/"

    def post_role(self, new_role):
        return self.post(url=f"{self.user_url}", json=new_role)

    def get_role(self, role_id, headers=None):
        return self.get(url=f"{self.user_url}{role_id}")

    def get_all_roles(self, headers=None):
        return self.get(url=f"{self.user_url}")

    def put_role(self, role_id, new_name):
        return self.put(url=f"{self.user_url}{role_id}", json=new_name)

    def delete_role(self, role_id):
        return self.delete(url=f"{self.user_url}{role_id}")