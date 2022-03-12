import requests
import os


class IssuesApiClient:
    Base_URL = 'http://127.0.0.1:8001/'
    LIST_CREATE_PREFIX = 'issues/'
    path_list_create = os.path.join(Base_URL, LIST_CREATE_PREFIX)

    def get_all_issues(self):
        res = requests.get(self.path_list_create)
        return res

    def get_issues(self, limit, offset):
        params = {'limit': limit, "offset": offset}
        res = requests.get(self.path_list_create, params)
        return res

    def get_issue_by_id(self, pk):
        path = os.path.join(self.path_list_create, str(pk))
        res = requests.get(path)
        return res

    def create_issue(self, name):
        params = {'name': name}
        res = requests.post(self.path_list_create, params)
        return res

    def put_issue(self, pk, name):
        params = {'name': name}
        path = os.path.join(self.path_list_create, str(pk))
        res = requests.put(path, params)
        return res

    def patch_issue(self, pk, name):
        params = {'name': name}
        path = os.path.join(self.path_list_create, str(pk))
        res = requests.patch(path, params)
        return res
