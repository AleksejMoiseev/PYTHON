from API_CLIET.issues_client import IssuesApiClient

client = IssuesApiClient()


class TestIssuesApiClient:

    def test_get_all_issues(self):
        responce = client.get_all_issues()
        assert responce.status_code == 200
        data = responce.json()
        assert type(data) is list
        assert len(data) != 0

    def test_check_limit_offset(self, limit, offset, expected_value_id_1):
        responce = client.get_issues(limit=limit, offset=offset)
        assert responce.status_code == 200
        assert responce.json() == expected_value_id_1

    def test_get_issue_by_id(self, expected_value_for_create):
        responce = client.get_issue_by_id(pk=1)
        assert responce.status_code == 200
        assert responce.json() == expected_value_for_create

    def test_create_issue(self, expected_value_for_create):
        responce = client.create_issue(expected_value_for_create['name'])
        assert responce.status_code == 200
        data = responce.json()
        assert data['name'] == expected_value_for_create['name']

    def test_put_issue(self, expected_value_for_create):
        responce = client.put_issue(pk=expected_value_for_create['id'], name=expected_value_for_create['name'])
        assert responce.status_code == 200
        assert responce.json() == expected_value_for_create

    def test_patch_issue(self, expected_value_for_create):
        responce = client.patch_issue(pk=expected_value_for_create['id'], name=expected_value_for_create['name'])
        assert responce.status_code == 200
        assert responce.json() == expected_value_for_create

    def test_negative_get_issue_id(self, expected_exception):
        responce = client.get_issue_by_id(pk=40)
        assert responce.status_code == 404
        assert responce.json() == expected_exception

    def test_negative_put_issue(self, expected_exception):
        responce = client.put_issue(pk=100, name='Alex')
        assert responce.status_code == 404
        assert responce.json() == expected_exception
